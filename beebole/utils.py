from enum import Enum


def to_dict(obj) -> dict:
    obj = vars(obj)
    for key, value in obj.items():
        if '__dataclass_params__' in dir(value):
            obj[key] = to_dict(value)
        if isinstance(value, Enum):
            obj[key] = value.value
    return obj


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Sentinel:
    ...


def service(service_name):
    def wrapper(method):
        nonlocal service_name
        method.__servicename__ = service_name
        return method
    return wrapper
