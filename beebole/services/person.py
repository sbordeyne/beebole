from beebole.base import BaseService
from beebole.utils import to_dict
from beebole.interfaces.entities.person import Person
from beebole.interfaces.responses import IdResponse, SimpleResponse, CustomFieldListResponse, GroupListResponse


class PersonService(BaseService):
    name: str = 'person'

    def create(self, person: Person) -> IdResponse:
        '''Create a new person.'''
        person_payload = to_dict(person)
        del person_payload['id']
        return {'person': person_payload}

    def get(self, person_id: int):  #TODO: Add return type
        '''Get a person by its ID'''
        return {'id': person_id}

    def update(self, person: Person) -> SimpleResponse:
        '''Update a person's data'''
        return {'person': to_dict(person)}

    def list(self, company_id: int):  #TODO: Add return type
        '''List people in a company'''
        return {'company': {'id': company_id}}

    def leaders(self, person_id: int):  #TODO: Add return type
        '''List the leaders of a person'''
        return {'id': person_id}

    def activate(self, person_id: int) -> SimpleResponse:
        '''Activate a person'''
        return {'id': person_id}

    def deactivate(self, person_id: int) -> SimpleResponse:
        '''Deactivate a person'''
        return {'id': person_id}

    def add_group(self, person_id: int, group_id: int) -> SimpleResponse:
        '''Add a person to a group by its id'''
        return {'id': person_id, 'group': {'id': group_id}}

    def remove_group(self, person_id: int, group_id: int) -> SimpleResponse:
        '''Remove a person from a group by its id'''
        return {'id': person_id, 'group': {'id': group_id}}

    def groups(self, person_id: int) -> GroupListResponse:
        '''List the groups a person is into'''
        return {'id': person_id}

    def set_custom_field_value(self, person_id: int, custom_field_id: int, custom_field_value: str) -> SimpleResponse:
        '''Set a custom field on that person'''
        return {
            'id': person_id,
            'customField': {
                'id': custom_field_id,
                'value': custom_field_value
            }
        }

    def clear_custom_field_value(self, person_id: int, custom_field_id: int) -> SimpleResponse:
        '''Clears the custom field on that person'''
        return {'id': person_id, 'customField': {'id': custom_field_id}}

    def custom_fields(self, person_id: int) -> CustomFieldListResponse:
        '''List the custom fields of that person'''
        return {'id': person_id}
