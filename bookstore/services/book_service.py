from typing import List

import requests
from requests import Response

from bookstore.models.models import Book

BOOKSTORE_V1_URL = "https://demoqa.com/BookStore/v1"
BOOK_ENDPOINT = f'{BOOKSTORE_V1_URL}/Book'
BOOKS_ENDPOINT = f'{BOOKSTORE_V1_URL}/Books'


def get_all_books() -> List[Book]:
    response = requests.get(BOOKS_ENDPOINT)
    if not response.ok:
        raise ConnectionError(f'Unable to get all books: {response.content}')
    books = response.json()['books']
    return [Book(**book) for book in books]


def get_book_by_isbn(isbn: str) -> Book:
    # response = requests.get(f'{BOOK_ENDPOINT}?ISBN={isbn}')
    response = requests.get(BOOK_ENDPOINT, params={'ISBN': isbn})
    if not response.ok:
        raise ConnectionError(f'Unable to get a book: {response.content}')
    return Book(**response.json())


def add_books_to_user(user_id, token, books: List[Book]):
    isbns = [{'isbn': book.isbn} for book in books]
    response = _add_books_endpoint(user_id, token, isbns)
    return response


def add_books_to_user_by_isbns(user_id, token, isbns: List[str]):
    isbns = [{'isbn': isbn} for isbn in isbns]
    response = _add_books_endpoint(user_id, token, isbns)
    return response


def _add_books_endpoint(user_id, token, isbn_objects) -> Response:
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
      "userId": user_id,
      "collectionOfIsbns": isbn_objects
    }
    response = requests.post(BOOKS_ENDPOINT, headers=headers, json=payload)
    if response.ok is False:
        raise ConnectionError(f'Unable to add books to user: {response.content}')
    return response


def delete_all_books_from_user(user_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'UserId': user_id}
    response = requests.delete(BOOKS_ENDPOINT, headers=headers, params=params)
    # response = requests.delete(f'{BOOKS_ENDPOINT}?UserId={user_id}', headers=headers)
    if not response.ok:
        raise ConnectionError(f'Unable to delete books: {response.content}')
    return response
