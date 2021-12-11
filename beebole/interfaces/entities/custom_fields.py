from dataclasses import dataclass

from beebole.interfaces.entities import IdEntity


@dataclass
class CustomField(IdEntity):
    name: str
    availableFor: str
