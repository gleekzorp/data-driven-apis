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


@pytest.fixture
def new_authorized_user(credentials):
    user, token = account_service.create_authorized_user(**credentials)
    yield user, token
    account_service.delete_user(user.userID, token.token)


@pytest.fixture
def new_unauthorized_user(credentials):
    user = account_service.create_user(**credentials)
    yield user
    # Need to authorize them before deleting
    token = account_service.generate_token(**credentials)
    account_service.delete_user(user.userID, token.token)


def test_create_user(credentials):
    user = account_service.create_user(**credentials)
    assert user.username == credentials.get('username')


def test_generate_token(credentials):
    account_service.create_user(**credentials)
    token = account_service.generate_token(**credentials)
    assert token.status == 'Success'


def test_create_authorized_user(credentials):
    account_service.create_authorized_user(**credentials)
    assert account_service.is_authorized(**credentials)


def test_create_unauthorized_user(credentials):
    account_service.create_user(**credentials)
    assert account_service.is_authorized(**credentials) is False


def test_delete_authorized_user(credentials):
    user, token = account_service.create_authorized_user(**credentials)
    response = account_service.delete_user(user.userID, token.token)
    assert response.ok


def test_cannot_delete_unauthorized_user(credentials):
    user = account_service.create_user(**credentials)
    with pytest.raises(ConnectionError):
        account_service.delete_user(user.userID, None)


def test_get_user():
    pytest.xfail()
