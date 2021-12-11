from dataclasses import dataclass

from beebole.interfaces.responses.simple import SimpleResponse
from beebole.interfaces.entities.jobs import JobInfo


@dataclass
class JobInfoResponse(SimpleResponse):
    job: JobInfo