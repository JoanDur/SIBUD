from typing import List
from backendpython.models.fines import FineDTO
from repositories.fine_repository import FineRepository

class FineService:
    def __init__(self):
        self.repository = FineRepository()

    def get_all(self) -> List[FineDTO]:
        return self.repository.get_all_fines() or []

    def get_by_user(self, user_id: str) -> List[FineDTO]:
        return self.repository.get_fines_by_user(user_id)

    def add_fine(self, fine: FineDTO):
        self.repository.add_fine(fine)

    def mark_as_paid(self, loan_id: str):
        self.repository.mark_as_paid(loan_id)

    def clear_fines(self):
        self.repository.clear_all_fines()
