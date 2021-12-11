from beebole.base import BaseService
from beebole.interfaces.responses import IdResponse, SimpleResponse, CustomFieldListResponse, GroupListResponse


class CompanyService(BaseService):
    name: str = 'company'

    def create(self, name: str, corporate: bool = False) -> IdResponse:
        return {'name': name, 'corporate': corporate}

    def get(self, company_id: int):  #TODO: Add return type
        return {'id': company_id}

    def list(self):  #TODO: Add return type
        return {}

    def activate(self, company_id: int) -> SimpleResponse:
        return {'id': company_id}

    def deactivate(self, company_id: int) -> SimpleResponse:
        return {'id': company_id}

    def attach_specific_task(self, company_id: int, task_id: int) -> SimpleResponse:
        return {'id': company_id, 'tasks': {'id': task_id}}

    def detach_specific_task(self, company_id: int, task_id: int) -> SimpleResponse:
        return {'id': company_id, 'tasks': {'id': task_id}}

    def specific_tasks(self, company_id: int):  #TODO: Add return type
        return {'id': company_id}

    def enable_specific_tasks(self, company_id: int) -> SimpleResponse:
        return {'id': company_id}

    def disable_specific_tasks(self, company_id: int) -> SimpleResponse:
        return {'id': company_id}

    def attach_member(self, company_id: int, member_id: int) -> SimpleResponse:
        return {'id': company_id, 'person': {'id': member_id}}

    def detach_member(self, company_id: int, member_id: int) -> SimpleResponse:
        return {'id': company_id, 'person': {'id': member_id}}

    def members(self, company_id: int):  #TODO: Add return type
        return {'id': company_id}

    def add_group(self, company_id: int, group_id: int) -> SimpleResponse:
        return {'id': company_id, 'group': {'id': group_id}}

    def remove_group(self, company_id: int, group_id: int) -> SimpleResponse:
        return {'id': company_id, 'group': {'id': group_id}}

    def groups(self, company_id: int) -> GroupListResponse:
        return {'id': company_id}

    def set_custom_field_value(self, company_id: int, custom_field_id: int, custom_field_value: str) -> SimpleResponse:
        return {
            'id': company_id,
            'customField': {
                'id': custom_field_id,
                'value': custom_field_value
            }
        }

    def clear_custom_field_value(self, company_id: int, custom_field_id: int) -> SimpleResponse:
        return {
            'id': company_id,
            'customField': {
                'id': custom_field_id,
            }
        }

    def custom_fields(self, company_id: int) -> CustomFieldListResponse:
        return {'id': company_id}
