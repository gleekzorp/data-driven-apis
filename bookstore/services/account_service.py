import requests

from bookstore.models.models import User

ACCOUNT_V1_URL = "https://demoqa.com/Account/v1"


def create_user(username, password) -> User:
    payload = {'userName': username, 'password': password}
    response = requests.post(f'{ACCOUNT_V1_URL}/User', json=payload)
    if not response.ok:
        raise ConnectionError(f'Unable to create user: {response.content}')
    return User(**response.json())
