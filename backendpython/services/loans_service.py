"""Loan Service.

Handles the business logic for loans.

Author: [Joan Sebastian Duran Pradilla <<jsduranp@udistirtal.edu.co >>]
"""
from typing import List
from backendpython.models.loans import LoanDTO
from repositories.loans_repository import LoanRepository

class LoanService:
    def __init__(self):
        self.repository = LoanRepository()

    def get_all(self) -> List[LoanDTO]:
        return self.repository.get_all_loans()

    def get_loans_by_user(self, user_id: str) -> List[LoanDTO]:
        return self.repository.get_loans_by_user(user_id)

    def add_loan(self, loan: LoanDTO):
        self.repository.add_loan(loan)

    def return_book(self, book_isbn: str) -> bool:
        return self.repository.mark_as_returned(book_isbn)
