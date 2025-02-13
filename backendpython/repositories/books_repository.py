from typing import List
from models.books import BookDTO

class BookRepository:
    def get_all_books(self) -> List[BookDTO]:
        # Implementación para obtener todos los libros
        pass

    def get_by_title(self, title: str) -> List[BookDTO]:
        # Implementación para obtener libros por título
        pass

    def get_by_author(self, author: str) -> List[BookDTO]:
        # Implementación para obtener libros por autor
        pass

    def get_by_category(self, category: str) -> List[BookDTO]:
        # Implementación para obtener libros por categoría
        pass

    def add_book(self, book: BookDTO):
        # Implementación para añadir un libro
        pass

    def remove_book(self, isbn: str):
        # Implementación para eliminar un libro por ISBN
        pass
