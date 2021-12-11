from typing import Dict, Optional

from requests import Response


class BeeboleException(Exception):
    '''Base exception class for all Beebole errors.'''

class BeeboleAPIException(BeeboleException):
    '''General purpose exception for all Beebole API errors'''
    def __init__(self, response: Response, body: Optional[Dict[str, str]] = None):
        body = body or response.json() or {}
        self.message = body.get('message', 'No message found in the body')
        self.response = response
        self.body = body

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message


class BeeboleRateLimited(BeeboleException):
    '''Exception raised when the rate limit of the Beebole API is reached.'''


class BeeboleNotFound(BeeboleException):
    '''Exception raised when a resource cannot be found.'''
