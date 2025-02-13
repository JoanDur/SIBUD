"""This module contains the routes for the books API
    Author: Joan Duran

"""


from typing import List
import json
from fastapi import APIRouter, HTTPException
from models.books import BookDTO  
from services.books_service import BookService

router = APIRouter()
service = BookService()

@router.get("/books/all", response_model=List[BookDTO])
def get_all_books():
    return service.get_all()

@router.get("/books/by_title/{title}", response_model=List[BookDTO])
def get_by_title(title: str):
    return service.get_by_title(title)

@router.get("/books/by_author/{author}", response_model=List[BookDTO])
def get_by_author(author: str):
    return service.get_by_author(author)

@router.get("/books/by_category/{category}", response_model=List[BookDTO])
def get_by_category(category: str):
    return service.get_by_category(category)

@router.post("/books/add")
def add_book(book: BookDTO):
    service.add_book(book)
    return {"message": "Book added successfully"}

@router.delete("/books/remove/{isbn}")
def remove_book(isbn: str):
    service.remove_book(isbn)
    return {"message": "Book removed successfully"}
