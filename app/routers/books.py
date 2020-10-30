from fastapi import APIRouter
from bookstore.mocks import FASTAPI_MOCKED_BOOKS

router = APIRouter()


@router.get('/books', tags=['books'])
async def get_all_books():
    return FASTAPI_MOCKED_BOOKS
