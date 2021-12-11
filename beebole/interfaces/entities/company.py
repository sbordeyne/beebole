from dataclasses import dataclass


@dataclass
class CompanyProjects:
    count: int


@dataclass
class Company:
    id: int
    name: str
    projects: CompanyProjects
    active: bool
