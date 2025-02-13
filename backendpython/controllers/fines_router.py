"""Fine Controller.

Handles API requests related to fines.

Author: [Joan Sebastian Duran Pradilla]
"""

from fastapi import APIRouter
from typing import List
from backendpython.models.fines import FineDTO
from services.fines_service import FineService

router = APIRouter()
service = FineService()

@router.get("/fines/all", response_model=List[FineDTO])
def get_all_fines():
    return service.get_all()

@router.get("/fines/user/{user_id}", response_model=List[FineDTO])
def get_fines_by_user(user_id: str):
    return service.get_by_user(user_id)

@router.post("/fines/add")
def add_fine(fine: FineDTO):
    service.add_fine(fine)
    return {"message": "Fine added successfully"}

@router.put("/fines/pay/{loan_id}")
def pay_fine(loan_id: str):
    service.mark_as_paid(loan_id)
    return {"message": "Fine marked as paid"}
