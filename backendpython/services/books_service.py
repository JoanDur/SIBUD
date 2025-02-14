from typing import List
from models.books import BookDTO
from repositories.books_repository import BookRepository

# Service
class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def get_all(self) -> List[BookDTO]:
        return self.repository.get_all_books() or []

    def get_by_title(self, title: str) -> List[BookDTO]:
        return self.repository.get_by_title(title) or []

    def get_by_author(self, author: str) -> List[BookDTO]:
        return self.repository.get_by_author(author) or []

    def get_by_category(self, category: str) -> List[BookDTO]:
        return self.repository.get_by_category(category) or []

    def add_book(self, book: BookDTO):
        self.repository.add_book(book)

    def remove_book(self, isbn: str):
        self.repository.remove_book(isbn)
