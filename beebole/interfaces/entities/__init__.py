from dataclasses import dataclass
from enum import Enum


class TimeEntryEntityType(str, Enum):
    ABSENCE: str = 'absence'
    COMPANY: str = 'company'
    PROJECT: str = 'project'
    SUBPROJECT: str = 'subproject'


class EntityType(TimeEntryEntityType):
    TASK: str = 'task'
    PERSON: str = 'person'


@dataclass
class IdEntity:
    id: int


@dataclass
class CountEntity:
    count: int