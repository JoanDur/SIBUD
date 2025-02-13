import json
from flask import Blueprint, request, jsonify

books_bp = Blueprint('books', __name__)
BOOKS_FILE = 'books.json'

# Cargar libros desde archivo JSON
def load_books():
    try:
        with open(BOOKS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar libros en archivo JSON
def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

# Obtener todos los libros
@books_bp.route('/', methods=['GET'])
def get_books():
    books = load_books()
    return jsonify({'books': books})

# Agregar un nuevo libro
@books_bp.route('/', methods=['POST'])
def add_book():
    books = load_books()
    data = request.get_json()
    book_id = str(len(books) + 1)
    books[book_id] = {'title': data['title'], 'available': True}
    save_books(books)
    return jsonify({'message': 'Libro agregado', 'book': books[book_id]})

# Verificar disponibilidad de un libro
def check_availability(book_id):
    books = load_books()
    return books.get(book_id, {}).get('available', False)

# Marcar un libro como prestado
def mark_as_borrowed(book_id):
    books = load_books()
    if book_id in books:
        books[book_id]['available'] = False
        save_books(books)
