from beebole.base import BaseService
from beebole.interfaces.responses import (
    SimpleResponse, IdResponse, AbsenceListResponse,
    AbsenceResponse, GroupListResponse
)


class AbsenceService(BaseService):
    name: str = 'absence'

    def create(self, name: str, company_id: int) -> IdResponse:
        return {'absence': {'name': name, 'company': {'id': company_id}}}

    def get(self, absence_id: int) -> AbsenceResponse:
        return {'id': absence_id}

    def update(self, absence_id: int, name: str) -> SimpleResponse:
        return {'absence': {'id': absence_id, 'name': name}}

    def list(self, company_id: int) -> AbsenceListResponse:
        return {'company' : {'id' : company_id}}

    def activate(self, absence_id: int) -> SimpleResponse:
        return {'id': absence_id}

    def deactivate(self, absence_id: int) -> SimpleResponse:
        return {'id': absence_id}

    def add_group(self, absence_id: int, group_id: int) -> SimpleResponse:
        return {'id' : absence_id, 'group' : {'id' : group_id}}

    def remove_group(self, absence_id: int, group_id: int) -> SimpleResponse:
        return {'id' : absence_id, 'group' : {'id' : group_id}}

    def groups(self, absence_id: int) -> GroupListResponse:
        return {'id' : absence_id}
