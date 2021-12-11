from base64 import b64encode
from typing import Tuple

import requests

from beebole import __version__
from beebole.services import *


class BeeboleClient:
    '''API client for the Beebole API. Supply an API token to get started.'''
    def __init__(self, api_token: str) -> None:
        self.endpoint = 'https://beebole-apps.com/api/v2'
        self.session = requests.session()
        self.session.headers['Authorization'] = (
            f'Basic {b64encode(f"{api_token}:x".encode("utf8")).decode("utf8")}'
        )
        self.session.headers['Content-Type'] = 'application/json'
        self.session.headers['User-Agent'] = f'beebole.py/{__version__}'

    def _request(self, payload: dict) -> Tuple[dict, requests.Response]:
        '''Performs a request to the beebole API.'''
        response = self.session.post(self.endpoint, json=payload)
        return response

    @property
    def absence(self):
        '''Handles absences'''
        return AbsenceService(self)

    @property
    def company(self):
        '''Handles companies'''
        return CompanyService(self)

    @property
    def custom_field(self):
        '''Handles custom fields'''
        return CustomFieldService(self)

    @property
    def person(self):
        '''Handles people'''
        return PersonService(self)

    @property
    def project(self):
        '''Handles projects'''
        return ProjectService(self)

    @property
    def subproject(self):
        '''Handle sub-projects'''
        return SubprojectService(self)

    @property
    def task(self):
        '''Handles tasks'''
        return TaskService(self)

    @property
    def time_entry(self):
        '''Handles time entries'''
        return TimeService(self)
    time = time_entry

    @property
    def group(self):
        '''Handles groups'''
        return GroupService(self)
