"""Data Transfer Object (DTO) for Fines.

Author: [Joan Sebastian Duran Pradilla <<jsduranp@udistrita.edu.co>>]
"""

from pydantic import BaseModel

class FineDTO(BaseModel):
    user_id: str
    loan_id: str
    reason: str
    fine_date: str
    amount: float
    due_date: str
    paid: bool
