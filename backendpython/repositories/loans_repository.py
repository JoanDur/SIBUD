"""Loan Repository.

Handles the data storage and retrieval for loans.

Author: [Joan Sebastian Duran Pradilla <<jsduranp@udistrital.edu.co>>]
"""
import json
from typing import List
from backendpython.models.loans import LoanDTO
from environment_variables import EnvironmentVariables

class LoanRepository:
    def __init__(self):
        env = EnvironmentVariables()
        self.path_file = env.path_loans_data
        self._load_data()

    def _load_data(self):
        try:
            with open(self.path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def get_all_loans(self) -> List[LoanDTO]:
        return [LoanDTO(**loan) for loan in self.data]

    def get_loans_by_user(self, user_id: str) -> List[LoanDTO]:
        return [LoanDTO(**loan) for loan in self.data if loan["user_id"] == user_id]

    def add_loan(self, loan: LoanDTO):
        self.data.append(loan.dict())
        self._save_data()

    def mark_as_returned(self, book_isbn: str):
        for loan in self.data:
            if loan["book_isbn"] == book_isbn:
                loan["returned"] = True
                self._save_data()
                return True
        return False

    def _save_data(self):
        with open(self.path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
