from collections import defaultdict
from datetime import datetime
from typing import Optional, Union, List

from beebole.base import BaseService
from beebole.interfaces.responses import SimpleResponse, JobInfoResponse
from beebole.interfaces.entities import EntityType, TimeEntryEntityType
from beebole.interfaces.entities.time_entry import ShowType, TimeEntryStatus
from beebole.exceptions import BeeboleException
from beebole.utils import service


class TimeService(BaseService):
    name: str = 'time_entry'

    def get_entities(
        self, entity_id: int, entity_type: TimeEntryEntityType,
        date: Union[datetime, str, None] = None
    ):  #TODO: Add return type
        if date is None:
            date = datetime.today()
        if isinstance(date, datetime):
            date = datetime.strftime('%y-%m-%d')
        return {entity_type.value: {'id': entity_id}, 'date': date}

    def get_tasks(self, subproject_id: int, date: Union[datetime, str, None] = None): #TODO: Add return type
        if date is None:
            date = datetime.today()
        if isinstance(date, datetime):
            date = datetime.strftime('%y-%m-%d')
        return {'subproject': {'id': subproject_id}, 'date': date}

    def create(
        self, entity_id, entity_type: TimeEntryEntityType,
        hours: float, date: Union[datetime, str, None] = None,
        comment: str = '', task_id: Optional[int] = None
    ): #TODO: Add return type
        if date is None:
            date = datetime.today()
        if isinstance(date, datetime):
            date = datetime.strftime('%y-%m-%d')
        entry = {
            entity_type.value: {'id': entity_id},
            'date': date,
            'hours': hours,
            'comment': comment
        }
        if task_id is not None:
            entry['task'] = {'id': task_id}
        return entry

    def update(
        self, entry_id, hours: Optional[float] = None, date: Union[datetime, str, None] = None,
        comment: Optional[str] = None, task_id: Optional[int] = None,
        entity_id: Optional[int] = None,
        entity_type: Optional[TimeEntryEntityType] = None
    ): #TODO: Add return type
        if isinstance(date, datetime):
            date = datetime.strftime('%y-%m-%d')

        entry = {'id': entry_id}
        if entity_type is not None and entity_id is not None:
            entry[entity_type.value] = {'id': entity_id}
        if hours is not None:
            entry['hours'] = hours
        if comment is not None:
            entry['comment'] = comment
        if task_id is not None:
            entry['task'] = {'id': task_id}
        if date is not None:
            entry['date'] = date
        return entry

    def delete(self, entry_id: int, date: Union[datetime, str, None] = None) -> SimpleResponse:
        if date is None:
            date = datetime.today()
        if isinstance(date, datetime):
            date = datetime.strftime('%y-%m-%d')
        return {'id': entry_id, 'date': date}

    def list(
        self, person_id: int, from_: Union[datetime, str],
        to: Union[datetime, str]
    ): #TODO: Add return type
        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'from': from_, 'to': to}

    def submit(
        self, person_id: int, from_: Union[datetime, str],
        to: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'from': from_, 'to': to}

    def approve(
        self, person_id: int, from_: Union[datetime, str],
        to: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'from': from_, 'to': to}

    def reject(
        self, person_id: int, from_: Union[datetime, str],
        to: Union[datetime, str], memo: str = ''
    ) -> SimpleResponse:
        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')
        return {
            'person': {'id': person_id},
            'from': from_,
            'to': to,
            'memo': memo
        }

    def lock(
        self, person_id: int, from_: Union[datetime, str],
        to: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'from': from_, 'to': to}

    def unlock(
        self, person_id: int, from_: Union[datetime, str],
        to: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'from': from_, 'to': to}

    @service('submit')
    def submit_by_id(
        self, person_id: int, entry_id: int,
        date: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'id': entry_id, 'date': date}

    @service('approve')
    def approve_by_id(
        self, person_id: int, entry_id: int,
        date: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'id': entry_id, 'date': date}

    @service('reject')
    def reject_by_id(
        self, person_id: int, entry_id: int,
        date: Union[datetime, str], memo: str = ''
    ) -> SimpleResponse:
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')
        return {
            'person': {'id': person_id},
            'id': entry_id,
            'date': date,
            'memo': memo
        }

    @service('lock')
    def lock_by_id(
        self, person_id: int, entry_id: int,
        date: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'id': entry_id, 'date': date}

    @service('unlock')
    def unlock_by_id(
        self, person_id: int, entry_id: int,
        date: Union[datetime, str]
    ) -> SimpleResponse:
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')
        return {'person': {'id': person_id}, 'id': entry_id, 'date': date}

    def export(
        self, from_: Union[datetime, str],
        to: Union[datetime, str], keys: List[str], show: ShowType = ShowType.ALL,
        status_filters: int = None, group_ids: List[int] = None,
        output_format: Optional[str] = None, entity_id: Optional[int] = None,
        entity_type: Optional[EntityType] = None
    ) -> JobInfoResponse:
        DEFAULT = lambda _: (ShowType.ALL, ShowType.ABSENCE, ShowType.WORK)
        ALL = (ShowType.ALL, ShowType.ABSENCE, ShowType.QUOTA, ShowType.WORK)
        QUOTA = (ShowType.QUOTA,)

        allowed_show_keys = defaultdict(
            DEFAULT,
            {
                'company': ALL, 'companyId': ALL, 'person': ALL,
                'personId': ALL, 'absence': ALL, 'absenceId': ALL,
                'inDays': ALL, 'available': QUOTA, 'balance': QUOTA,
                'taken': QUOTA, 'availableInDays': QUOTA,
                'balanceInDays': QUOTA, 'takenInDays': QUOTA, 'fromTo': QUOTA
            }
        )
        for k in keys:
            if show not in allowed_show_keys[k]:
                raise BeeboleException(
                    f"Can't start export : {k} is not allowed for show {show.value}"
                )

        if isinstance(from_, datetime):
            from_ = from_.strftime('%Y-%m-%d')
        if isinstance(to, datetime):
            to = to.strftime('%Y-%m-%d')

        export = {
            'from': from_,
            'to': to,
            'show': show.value,
            'keys': keys,
        }

        if status_filters is not None:
            # This complicated looking thing is actually the code that handles
            # bit-masking for statuses.
            # Step 1 : convert the argument to binary, strip the '0b', and fill
            #          with 0 to the length of the enum (total number of flags)
            status_mask = bin(status_filters)[2:].zfill(len(TimeEntryStatus))
            # Step 2 : iterate over the bit mask and the enum, sorted with
            #          highest-order bits first. If the bitmask is at 1 for
            #          that enum, add the name to the resulting array,
            #          otherwise skip it.
            status_filters = [
                s.name.lower()
                for m, s in zip(
                    status_mask, sorted(
                        TimeEntryStatus, key=lambda k: k.value, reverse=True
                    )
                )
                if int(m)
            ]
            export['statusFilters'] = status_filters

        if entity_type is not None and entity_id is not None:
            export[entity_type.value] = {'id': entity_id}
        if group_ids is not None and group_ids:
            export['gids'] = group_ids
        if output_format is not None and output_format == 'array':
            export['outputFormat'] = output_format
        return export

    def get_job_info(self, job_id: int, output_format: Optional[str] = None) -> JobInfoResponse:
        info = {'id': job_id}
        if output_format is not None and output_format == 'array':
            info['outputFormat'] = output_format
        return info
