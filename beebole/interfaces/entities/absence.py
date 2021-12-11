from dataclasses import dataclass

from beebole.interfaces.entities import IdEntity


@dataclass
class Absence(IdEntity):
    name: str
    company: IdEntity
    active: bool
