import pytest
from services.books_service import BookService
from models.books import BookDTO

@pytest.fixture
def book_service():
    return BookService()

def test_add_book(book_service):
    book = BookDTO(title="Test Book", author="Joan Duranbb", category="Ficcion", isbn="12345", available=True)
    book_service.add_book(book)
    books = book_service.get_all()
    assert any(b.isbn == "12345" for b in books)

def test_remove_book(book_service):
    book_service.remove_book("12345")
    books = book_service.get_all()
    assert not any(b.isbn == "12345" for b in books)
