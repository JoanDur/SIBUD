import pytest
from backendpython.models.loans import LoanDTO
from backendpython.services.loans_service import LoanService
from datetime import datetime

@pytest.fixture
def loan_service():
    return LoanService()

def test_create_loan(loan_service):
    loan = LoanDTO(user_id="1", book_isbn="12345", loan_date=str(datetime.now().date()), return_date=str(datetime.now().date()), returned=False)
    loan_service.add_loan(loan)
    loans = loan_service.get_all()
    assert loans is not None
    assert any(l.book_isbn == "12345" for l in loans)

def test_return_loan(loan_service):
    loan = LoanDTO(user_id="1", book_isbn="12345", loan_date=str(datetime.now().date()), return_date=str(datetime.now().date()), returned=False)
    loan_service.add_loan(loan)
    loan_service.return_book("12345")
    loans = loan_service.get_all()
    assert loans is not None
    assert all(l.return_date is not None for l in loans if l.book_isbn == "12345")
