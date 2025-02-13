"""This module has a class to handle environment variables in the project.

Author: [Joan Sebastian Duran Pradilla]
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

class EnvironmentVariables:
    """This class is used to handle environment variables."""
    
    def __init__(self):
        self.path_books_data = os.getenv("PATH_BOOKS_DATA", "data/books.json")
        self.path_loans_data = os.getenv("PATH_LOANS_DATA", "data/loans.json")
        self.path_fines_data = os.getenv("PATH_FINES_DATA", "data/fines.json")
        self.path_users_data = os.getenv("PATH_USERS_DATA", "data/users.json")
        self.path_notifications_data = os.getenv("PATH_NOTIFICATIONS_DATA", "data/notifications.json")
