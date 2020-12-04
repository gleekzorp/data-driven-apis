from typing import Dict

import pytest

from bookstore.models.models import Book
from bookstore.mocks import MOCKED_BOOKS
from bookstore.services import account_service, book_service


@pytest.fixture
def login_seam(py, new_authorized_user):
    def _login(next_url_path):
        base_url = 'https://demoqa.com'
        user, token = new_authorized_user
        py.visit(f'{base_url}/login')
        py.set_cookie({'name': 'userName', 'value': user.username})
        py.set_cookie({'name': 'userID', 'value': user.userID})
        py.set_cookie({'name': 'token', 'value': token.token})
        py.set_cookie({'name': 'expires', 'value': token.expires})
        py.visit(f'{base_url}{next_url_path}')
        return user, token
    return _login


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


@pytest.fixture
def mocked_books():
    return [Book(**book) for book in MOCKED_BOOKS]
