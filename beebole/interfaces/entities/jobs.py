from dataclasses import dataclass
from typing import Optional

from beebole.interfaces.entities import IdEntity


@dataclass
class JobInfo(IdEntity):
    status: str
    result: Optional[str]
