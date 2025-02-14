"""Data Transfer Object (DTO) for Loans.

Author: [Joan Sebastian Duran Pradilla]
"""

from pydantic import BaseModel
from datetime import date

class LoanDTO(BaseModel):
    user_id: str
    book_isbn: str
    loan_date: str
    return_date: str
    returned: bool
