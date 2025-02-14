import pytest
from backendpython.models.books import BookDTO
from backendpython.services.books_service import BookService

@pytest.fixture
def book_service():
    return BookService()

def test_add_book(book_service):
    book = BookDTO(title="Test Book", author="John Doe", category="Fiction", isbn="12345", available=True)
    book_service.add_book(book)
    books = book_service.get_all()
    assert books is not None
    assert any(b.isbn == "12345" for b in books)

def test_remove_book(book_service):
    book = BookDTO(title="Test Book", author="John Doe", category="Fiction", isbn="12345", available=True)
    book_service.add_book(book)
    book_service.remove_book("12345")
    books = book_service.get_all()
    assert books is not None
    assert not any(b.isbn == "12345" for b in books)
