from beebole.base import BaseService
from beebole.interfaces.responses import IdResponse, SimpleResponse, GroupListResponse


class TaskService(BaseService):
    name: str = 'task'

    def create(self, name: str, company_id: int) -> IdResponse:
        return {'task': {'name': name, 'company': {'id': company_id}}}

    def get(self, task_id: int):  #TODO: Add return type
        return {'id': task_id}

    def update(self, task_id: int, name: str) -> SimpleResponse:
        return {'task': {'id': task_id, 'name': name}}

    def list(self, company_id: int):  #TODO: Add return type
        return {'company': {'id': company_id}}

    def activate(self, task_id: int) -> SimpleResponse:
        return {'id': task_id}

    def deactivate(self, task_id: int) -> SimpleResponse:
        return {'id': task_id}

    def add_group(self, task_id: int, group_id: int) -> SimpleResponse:
        return {'id': task_id, 'group': {'id': group_id}}

    def remove_group(self, task_id: int, group_id: int) -> SimpleResponse:
        return {'id': task_id, 'group': {'id': group_id}}

    def groups(self, task_id: int) -> GroupListResponse:
        return {'id': task_id}
