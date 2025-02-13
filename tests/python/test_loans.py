import pytest
from models.loan import LoanDTO
from services.loans_service import LoanService
from datetime import datetime

@pytest.fixture
def loan_service():
    return LoanService()

def test_create_loan(loan_service):
    loan = LoanDTO(user_id="1", book_isbn="12345", loan_date=str(datetime.now()), return_date=None)
    loan_service.create_loan(loan)
    loans = loan_service.get_all_loans()
    assert any(l.book_isbn == "12345" for l in loans)

def test_return_loan(loan_service):
    loan_service.return_loan("12345")
    loans = loan_service.get_all_loans()
    assert all(l.return_date is not None for l in loans if l.book_isbn == "12345")
