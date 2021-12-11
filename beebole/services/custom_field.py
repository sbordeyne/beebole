from beebole.base import BaseService
from beebole.interfaces.responses import CustomFieldListResponse

class CustomFieldService(BaseService):
    name: str = 'custom_field'

    def list(self) -> CustomFieldListResponse:
        '''List custom fields'''
        return {}
