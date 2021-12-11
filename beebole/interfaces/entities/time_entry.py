from enum import Enum, IntFlag


class ShowType(str, Enum):
    ALL = 'all'
    ABSENCE = 'abs'
    QUOTA = 'quota'
    WORK = 'work'


class TimeEntryStatus(IntFlag):
    A = 1
    D = 2
    L = 4
    R = 8
    S = 16
