from dataclasses import dataclass
from typing import List

from beebole.interfaces.responses import SimpleResponse
from beebole.interfaces.entities.group import Group, ParentedGroup


@dataclass
class GroupResponse(SimpleResponse):
    group: ParentedGroup


@dataclass
class GroupListResponse(SimpleResponse):
    groups: List[Group]
