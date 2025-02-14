from typing import List
from models.books import BookDTO

class BookRepository:
    def __init__(self):
        self.books = []

    def get_all_books(self) -> List[BookDTO]:
        return self.books

    def get_by_title(self, title: str) -> List[BookDTO]:
        return [book for book in self.books if book.title == title]

    def get_by_author(self, author: str) -> List[BookDTO]:
        return [book for book in self.books if book.author == author]

    def get_by_category(self, category: str) -> List[BookDTO]:
        return [book for book in self.books if book.category == category]

    def add_book(self, book: BookDTO):
        self.books.append(book)

    def remove_book(self, isbn: str):
        self.books = [book for book in self.books if book.isbn != isbn]
