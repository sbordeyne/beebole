from base64 import b64encode

def test_api_key_encoding(client, correct_api_key):
    calc = b64encode(
        f'{correct_api_key}:x'.encode('utf8')
    ).decode('utf8')
    header = f'Basic {calc}'
    assert header == client.session.headers['Authorization'], 'Authorization header does not match expected header'


def test_correct_api_key(client):
    ...
