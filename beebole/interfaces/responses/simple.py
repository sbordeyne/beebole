from dataclasses import dataclass

@dataclass
class SimpleResponse:
    status: str


@dataclass
class IdResponse(SimpleResponse):
    id: int
