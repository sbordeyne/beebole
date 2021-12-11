from datetime import datetime
from typing import Union, Optional

from beebole.base import BaseService
from beebole.interfaces.responses import (
    IdResponse, SimpleResponse, CustomFieldListResponse, GroupListResponse,
)


class ProjectService(BaseService):
    name: str = 'project'

    def create(
        self, name: str, company_id: int, description: str = '',
        start_date: Union[datetime, None, str] = None
    ) -> IdResponse:
        if start_date is None:
            now = datetime.now()
            start_date = datetime(now.year, now.month, 1, 1, 0, 0, 0)
        start_date: str = (
            start_date.strftime('%Y-%m-%d')
            if isinstance(start_date, datetime)
            else start_date
        )
        return {
            'project': {
                'name': name,
                'startDate': start_date,
                'description': description,
                'company': {'id': company_id}
            }
        }

    def get(self, project_id: int):  #TODO: Add return type
        return {'id': project_id}

    def update(
        self, project_id: int, name: Optional[str] = None,
        start_date: Union[datetime, None, str] = None,
        description: Optional[str] = None
    ) -> SimpleResponse:
        '''Update a project by its ID.'''
        project = {'id': project_id}
        if name is not None:
            project['name'] = name
        if start_date is not None:
            project['startDate'] = (
                start_date.strftime('%Y-%m-%d')
                if isinstance(start_date, datetime)
                else start_date
            )
        if description is not None:
            project['description'] = description
        return {'project' : project}

    def list(self, company_id: int):  #TODO: Add return type
        return {'company': {'id' : company_id}}

    def activate(self, project_id: int) -> SimpleResponse:
        return {'id': project_id}

    def deactivate(self, project_id: int) -> SimpleResponse:
        return {'id': project_id}

    def attach_specific_tasks(self, project_id: int, task_id: int) -> SimpleResponse:
        return {'id': project_id, 'task': {'id': task_id}}

    def detach_specific_tasks(self, project_id: int, task_id: int) -> SimpleResponse:
        return {'id': project_id, 'task': {'id': task_id}}

    def specific_tasks(self, project_id: int):  #TODO: Add return type
        return {'id': project_id}

    def enable_specific_tasks(self, project_id: int) -> SimpleResponse:
        return {'id': project_id}

    def disable_specific_tasks(self, project_id: int) -> SimpleResponse:
        return {'id': project_id}

    def attach_member(
        self, project_id: int, member_id: int, group: bool = False
    ) -> SimpleResponse:
        person_or_group = 'group' if group else 'person'
        return {'id': project_id, person_or_group: {'id' : member_id}}

    def detach_member(
        self, project_id: int, member_id: int, group: bool = False
    ) -> SimpleResponse:
        person_or_group = 'group' if group else 'person'
        return {'id': project_id, person_or_group: {'id' : member_id}}

    def members(self, project_id: int):  #TODO: Add return type
        return {'id': project_id}

    def attach_manager(self, project_id: int, member_id: int) -> SimpleResponse:
        return {'id': project_id, 'person': {'id' : member_id}}

    def detach_manager(self, project_id: int, member_id: int) -> SimpleResponse:
        return {'id': project_id, 'person': {'id' : member_id}}

    def managers(self, project_id: int):
        return {'id': project_id}

    def add_group(self, project_id: int, group_id: int) -> SimpleResponse:
        return {'id': project_id, 'group': {'id': group_id}}

    def remove_group(self, project_id: int, group_id: int) -> SimpleResponse:
        return {'id': project_id, 'group': {'id': group_id}}

    def groups(self, project_id: int) -> GroupListResponse:
        return {'id': project_id}

    def set_custom_field_value(
        self, project_id: int, custom_field_id: int,
        custom_field_value: str
    ) -> SimpleResponse:
        return {
            'id': project_id,
            'customField': {
                'id': custom_field_id,
                'value': custom_field_value
            }
        }

    def clear_custom_field_value(
        self, project_id: int, custom_field_id: int
    ) -> SimpleResponse:
        return {
            'id': project_id,
            'customField': {
                'id': custom_field_id,
            }
        }

    def custom_fields(self, project_id: int) -> CustomFieldListResponse:
        return {'id': project_id}
