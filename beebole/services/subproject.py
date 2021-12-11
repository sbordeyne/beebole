from beebole.base import BaseService
from beebole.interfaces.responses import (
    IdResponse, SimpleResponse, CustomFieldListResponse, GroupListResponse
)


class SubprojectService(BaseService):
    name: str = 'subproject'

    def create(self, name: str, project_id: int) -> IdResponse:
        return {'name': name,'project': {'id': project_id}}

    def get(self, subproject_id: int):  #TODO: Add return type
        return {'id': subproject_id}

    def update(self, subproject_id: int, name: str) -> SimpleResponse:
        '''Update a project by its ID.'''
        return {'subproject': {'name': name, 'id': subproject_id}}

    def list(self, project_id: int):  #TODO: Add return type
        return {'project': {'id' : project_id}}

    def activate(self, subproject_id: int) -> SimpleResponse:
        return {'id': subproject_id}

    def deactivate(self, subproject_id: int) -> SimpleResponse:
        return {'id': subproject_id}

    def attach_specific_tasks(self, subproject_id: int, task_id: int) -> SimpleResponse:
        return {'id': subproject_id, 'task': {'id': task_id}}

    def detach_specific_tasks(self, subproject_id: int, task_id: int) -> SimpleResponse:
        return {'id': subproject_id, 'task': {'id': task_id}}

    def specific_tasks(self, subproject_id: int):  #TODO: Add return type
        return {'id': subproject_id}

    def enable_specific_tasks(self, subproject_id: int) -> SimpleResponse:
        return {'id': subproject_id}

    def disable_specific_tasks(self, subproject_id: int) -> SimpleResponse:
        return {'id': subproject_id}

    def attach_member(
        self, subproject_id: int, member_id: int, group: bool = False
    ) -> SimpleResponse:
        person_or_group = 'group' if group else 'person'
        return {'id': subproject_id, person_or_group: {'id' : member_id}}

    def detach_member(
        self, subproject_id: int, member_id: int, group: bool = False
    ) -> SimpleResponse:
        person_or_group = 'group' if group else 'person'
        return {'id': subproject_id, person_or_group: {'id' : member_id}}

    def members(self, subproject_id: int):  #TODO: Add return type
        return {'id': subproject_id}

    def add_group(self, subproject_id: int, group_id: int) -> SimpleResponse:
        return {'id': subproject_id, 'group': {'id': group_id}}

    def remove_group(self, subproject_id: int, group_id: int) -> SimpleResponse:
        return {'id': subproject_id, 'group': {'id': group_id}}

    def groups(self, subproject_id: int) -> GroupListResponse:
        return {'id': subproject_id}

    def set_custom_field_value(
        self, subproject_id: int, custom_field_id: int,
        custom_field_value: str
    ) -> SimpleResponse:
        return {
            'id': subproject_id,
            'customField': {
                'id': custom_field_id,
                'value': custom_field_value
            }
        }

    def clear_custom_field_value(
        self, subproject_id: int, custom_field_id: int
    ) -> SimpleResponse:
        return {
            'id': subproject_id,
            'customField': {
                'id': custom_field_id,
            }
        }

    def custom_fields(self, subproject_id: int) -> CustomFieldListResponse:
        return {'id': subproject_id}
