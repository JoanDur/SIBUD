"""Data Transfer Object (DTO) for Fines.

Author: [Joan Sebastian Duran Pradilla <<jsduranp@udistrita.edu.co>>]
"""

from pydantic import BaseModel
from datetime import date

class FineDTO(BaseModel):
    user_id: str
    loan_id: str
    amount: float
    reason: str
    fine_date: date
    paid: bool
