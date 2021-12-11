from dataclasses import dataclass
from typing import List

from beebole.interfaces.entities.custom_fields import CustomField


@dataclass
class CustomFieldListResponse:
    customFields: List[CustomField]
