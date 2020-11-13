from typing import Dict

import requests
import pytest

from bookstore.services import account_service


ACCOUNT_V1_URL = "https://demoqa.com/Account/v1"


@pytest.fixture
def credentials(fake) -> Dict:
    username = fake.first_name() + fake.last_name()
    password = 'P@$$w0rd'
    return {'username': username, 'password': password}


def test_create_user(credentials):
    user = account_service.create_user(**credentials)
    assert user.username == credentials.get('username')


def test_create_authorized_user(credentials):
    # user_response = requests.post(f'{ACCOUNT_V1_URL}/User', json=credentials)
    # assert user_response.ok
    user_response = account_service.create_user(**credentials)
    token_response = requests.post(f'{ACCOUNT_V1_URL}/GenerateToken', json=credentials)
    assert token_response.ok
    auth_response = requests.post(f'{ACCOUNT_V1_URL}/Authorized', json=credentials)
    assert auth_response.ok
    assert auth_response.json() is True


def test_create_unauthorized_user(credentials):
    user_response = requests.post(f'{ACCOUNT_V1_URL}/User', json=credentials)
    assert user_response.ok
    auth_response = requests.post(f'{ACCOUNT_V1_URL}/Authorized', json=credentials)
    assert auth_response.ok
    assert auth_response.json() is False


def test_delete_user():
    pytest.xfail()


def test_get_user():
    pytest.xfail()
