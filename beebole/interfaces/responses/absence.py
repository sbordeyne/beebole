from dataclasses import dataclass
from typing import List

from beebole.interfaces.responses import SimpleResponse
from beebole.interfaces.entities.absence import Absence


@dataclass
class AbsenceResponse(SimpleResponse):
    absence: Absence


@dataclass
class AbsenceListResponse(SimpleResponse):
    absences: List[Absence]