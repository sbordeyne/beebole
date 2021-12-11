from inspect import Parameter, _ParameterKind, signature, Signature
from typing import Any, Callable, Optional, Tuple, Union, List, Dict

from dacite import Config, from_dict
from requests import Response

from beebole.interfaces.responses import SimpleResponse
from beebole.exceptions import (
    BeeboleException, BeeboleAPIException, BeeboleRateLimited,
    BeeboleNotFound,
)
from beebole.utils import Sentinel


# TODO: Handle rate limiting


class BaseService:
    name: str
    config: Optional[Config] = None

    def _get_service_name(self, method: Callable) -> str:
        '''Gets the name of the service from the method's dunders'''
        # Step 1: extract classname and method_name
        classname, method_name = method.__qualname__.split('.')
        if hasattr(method, '__servicename__'):
            method_name = method.__servicename__
        # Get the actual service class from its name (using __globals__ is a bit dirty)
        service_class: 'BaseService' = method.__globals__.get(classname)
        if service_class is None:
            # This should never happen in theory...
            raise BeeboleException('Service class not found')
        # get the name and format it into the final service name, i.e.
        # $service_name.$method_name ('person.add_group' for instance)
        service_name = service_class.name
        return f'{service_name}.{method_name}'

    def _add_keyword_argument(
        self, argname: str, default: Any, kwargs: dict,
        annotation: type,
    ) -> Tuple[dict, Any]:
        '''Add a keyword argument to a method. Handling is done in the decorator'''
        value = kwargs.pop(argname, Sentinel())
        if isinstance(value, Sentinel):
            value = getattr(self, argname, default)
        self.extra_args[argname] = Parameter(
            argname, _ParameterKind.KEYWORD_ONLY,
            default=default, annotation=annotation
        )
        return kwargs, value

    def _parse_api_response(
        self, response: Response, out_type: Optional[type] = None
    ) -> Union[dict, SimpleResponse]:
        '''
        Parses the API response using the return type of the method.
        Raises exceptions when applicable.
        '''
        body = response.json()
        if body['status'] == 'error' or response.status_code != 200:
            if response.status_code == 429:
                raise BeeboleRateLimited(response)
            if response.status_code == 404:
                raise BeeboleNotFound(response)
            # Raise an exception if the response is an error
            raise BeeboleAPIException(response)
        # If a return type is set in the annotations, parse the body of the
        # response with dacite. The config is set as part of a class attribute
        if out_type is not None and isinstance(out_type, type):
            return from_dict(
                out_type, body,
                config=self.config
            )
        return body

    def _do_cast(self, arg: Any, param: Parameter) -> Any:
        try:
            if isinstance(param.annotation, type):
                return param.annotation(arg)
            return globals()[param.annotation](arg)
        except KeyError:
            raise BeeboleException(
                f"Can't find type {param.annotation} globally."
            )
        except Exception:
            raise BeeboleException((
                f"Can't cast {param.name} into {param.annotation.__name__} "
                f"for argument of type {type(arg)} : {arg}"
            ))

    def _cast_input_args_or_raise(
        self, args: List[Any], kwargs: Dict[str, Any], signature: Signature
    ) -> Tuple[List[Any], Dict[str, Any]]:
        positional: List[Parameter] = []
        keyword: Dict[str, Parameter] = {}

        # Split keyword and positional arguments
        for param in signature.parameters.values():
            if param.kind in (_ParameterKind.POSITIONAL_ONLY, _ParameterKind.VAR_POSITIONAL):
                positional.append(param)
            elif param.kind in (_ParameterKind.KEYWORD_ONLY, _ParameterKind.VAR_KEYWORD):
                keyword[param.name] = param
            elif param.kind == _ParameterKind.POSITIONAL_OR_KEYWORD:
                if param.name in kwargs:
                    keyword[param.name] = param
                else:
                    positional.append(param)

        # Cast positional arguments
        for i, (arg, param) in enumerate(zip(args, positional)):
            args[i] = self._do_cast(arg, param)

        # Cast keyword arguments
        for argname, argvalue in kwargs.items():
            kwargs[argname] = self._do_cast(argvalue, keyword[argname])

        return args, kwargs

    def _requester(self, method: Callable):
        '''
        Decorator that takes in a service method, and make it do the actual
        request. Returns the response as a validated dataclass.

        Flow:
        - extract service name and method name from __qualname__
        - construct the full service name
        - fetch the payload by executing the method with its arguments
        - add the service key to the payload as fetched previously
        - perform the request
        - fetch the return type from the method's __annotations__
        - cast the response with the return type using dacite.

        Set the __doc__, __name__ and __annotations__ attributes on the
        wrapped method as to not interfere with static type checkers.
        Use the functools.wraps decorator to preserve the original signature.
        '''
        def wrapped(*args, **kwargs):
            service_name = self._get_service_name(method)
            # Extract the external keyword argument before running the method
            kwargs, is_external = self._add_keyword_argument(
                'external', False, kwargs, bool
            )
            # FIXME: Fix this to support typing.Union, Optional, Enums, etc.
            # args, kwargs = self._cast_input_args_or_raise(
            #     args, kwargs, signature(method)
            # )
            # Fetch the payload by running the wrapped method.
            payload: dict = method(*args, **kwargs)
            # Add the service to that payload (required by the API)
            payload['service'] = service_name
            if is_external and 'id' in payload:
                # Handle external IDs
                payload['xid'] = payload['id']
                del payload['id']
            # Perform the request using the client of the service
            response: Response = self.client._request(payload)
            return self._parse_api_response(
                response, method.__annotations__.get('return')
            )  # Return the raw body otherwise
        # Using inspect, get the signature of the original method
        sig = signature(method)
        # Hack to make the parameters dict mutable
        sig._parameters = dict(sig.parameters)
        # Add extra arguments to the signature
        sig._parameters.update(self.extra_args)
        # Finally, set all the documentation attributes of the wrapped method
        # to their original values. Helpful to not interfere with static type
        # checkers, and the help() built-in function.
        wrapped.__annotations__ = method.__annotations__
        wrapped.__doc__ = method.__doc__
        wrapped.__name__ = method.__name__
        wrapped.__signature__ = sig
        return wrapped

    def __init__(self, client, external: bool = False):
        self.client = client
        self.external = external
        self.extra_args = {}

        methods = (m for m in dir(self) if callable(getattr(self, m)))
        for method_name in methods:
            if method_name.startswith('_'):
                # Do not decorate private methods and dunders
                continue
            method = getattr(self, method_name)
            setattr(self, method_name, self._requester(method))
