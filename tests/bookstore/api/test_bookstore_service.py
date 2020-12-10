import pytest

from bookstore.services import book_service

BOOKSTORE_V1_URL = "https://demoqa.com/BookStore/v1"


def test_get_all_books():
    books = book_service.get_all_books()
    assert len(books) == 8  # There are 8 books seeded in the DB


def test_get_book_by_isbn():
    isbn = '9781449325862'
    book = book_service.get_book_by_isbn(isbn)
    assert isbn == book.isbn


def test_add_books_to_user(new_authorized_user, mocked_books):
    user, token = new_authorized_user
    response = book_service.add_books_to_user(user.userID, token.token, mocked_books)
    assert response.ok


def test_add_books_to_user_by_isbns():
    pytest.xfail()


def test_delete_all_books_from_user(new_authorized_user, mocked_books):
    user, token = new_authorized_user
    book_service.add_books_to_user(user.userID, token.token, mocked_books)
    response = book_service.delete_all_books_from_user(user.userID, token.token)
    assert response.ok


def test_delete_single_book_from_user():
    pytest.xfail()


def test_replace_book_in_collection_by_isbn():
    pytest.xfail()
