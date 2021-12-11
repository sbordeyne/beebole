from typing import Optional

from beebole.base import BaseService
from beebole.interfaces.responses import IdResponse, SimpleResponse, GroupResponse, GroupListResponse
from beebole.interfaces.entities import EntityType


class GroupService(BaseService):
    name: str = 'group'

    def create(self, name: str, parent_group_id: Optional[int] = None) -> IdResponse:
        group = {'name': name}
        if parent_group_id is not None:
            group['parent'] = {'id': parent_group_id}
        return group

    def get(self, group_id: int) -> GroupResponse:
        return {'id': group_id}

    def update(self, group_id: int, name: str) -> SimpleResponse:
        return {'group': {'id': group_id, 'name': name}}

    def delete(self, group_id: int, force: bool = False) -> SimpleResponse:
        return {'id': group_id, 'force': force}

    def list(self, entity_id: int, entity_type: EntityType) -> GroupListResponse:
        return {entity_type.value: entity_id}

    def assignments(self, group_id: int):  #TODO: Add return type
        return {'id': group_id}

    def tree(self): #TODO: Add return type
        return {}
