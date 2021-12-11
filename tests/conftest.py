import json
from pathlib import Path

from pytest import fixture

from beebole.client import BeeboleClient


def mocked_requester(_, payload: dict) -> dict:
    with open(Path(__file__).parent / 'data/responses.json') as infile:
        responses: dict = json.load(infile)
    return responses.get(
        payload.get('service'), {'status': 'error'}
    )


@fixture
def correct_api_key():
    return 'correct_api_key'


@fixture
def wrong_api_key():
    return 'wrong_api_key'


@fixture
def client(correct_api_key):
    client = BeeboleClient(correct_api_key)
    client.request = mocked_requester
    return client


@fixture
def wrong_client(wrong_api_key):
    return BeeboleClient(wrong_api_key)
