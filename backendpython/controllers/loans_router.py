"""Loan Controller.

Handles API requests related to loans.

Author: [Joan Sebastian Duran Pradilla <<jsduranp@udistrita.edu.co>> ]
"""
from fastapi import APIRouter, HTTPException
from typing import List
from backendpython.models.loans import LoanDTO
from services.loans_service import LoanService

router = APIRouter()
service = LoanService()

@router.get("/loans/all", response_model=List[LoanDTO])
def get_all_loans():
    return service.get_all()

@router.get("/loans/by_user/{user_id}", response_model=List[LoanDTO])
def get_loans_by_user(user_id: str):
    return service.get_loans_by_user(user_id)

@router.post("/loans/add")
def add_loan(loan: LoanDTO):
    service.add_loan(loan)
    return {"message": "Loan registered successfully"}

@router.put("/loans/return/{book_isbn}")
def return_book(book_isbn: str):
    success = service.return_book(book_isbn)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found or already returned")
    return {"message": "Book returned successfully"}
