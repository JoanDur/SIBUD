"""Fine Repository.

Handles the data storage and retrieval for fines.

Author: [Joan Sebastian Duran Pradilla <<jsduranp@udistrita.edu.co>>]
"""

import json
from typing import List
from backendpython.models.fines import FineDTO
from environment_variables import EnvironmentVariables

class FineRepository:
    def __init__(self):
        env = EnvironmentVariables()
        self.path_file = env.path_fines_data
        self._load_data()

    def _load_data(self):
        try:
            with open(self.path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def get_all_fines(self) -> List[FineDTO]:
        return [FineDTO(**fine) for fine in self.data]

    def get_fines_by_user(self, user_id: str) -> List[FineDTO]:
        return [FineDTO(**fine) for fine in self.data if fine["user_id"] == user_id]

    def add_fine(self, fine: FineDTO):
        self.data.append(fine.dict())
        self._save_data()

    def mark_as_paid(self, loan_id: str):
        for fine in self.data:
            if fine["loan_id"] == loan_id:
                fine["paid"] = True
                self._save_data()
                break

    def _save_data(self):
        with open(self.path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
