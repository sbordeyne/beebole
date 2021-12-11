from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from beebole.interfaces.entities import IdEntity


class UserGroup(str, Enum):
    ADMIN = 'admin'
    CONTRACTOR = 'contractor'
    EMPLOYEE = 'employee'
    PM = 'pm'
    LEADER = 'leader'


@dataclass
class Person(IdEntity):
    name: str
    leaders: 'List[Person]'
    email: Optional[str] = ''
    invite: Optional[bool] = False
    userGroup: UserGroup = UserGroup.EMPLOYEE
