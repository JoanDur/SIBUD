"""This module has a class to handle environment variables in the project.

Author: [Joan Duran]
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

class EnvironmentVariables:
    """This class is used to handle environment variables."""

    def __init__(self):
        """Initialize environment variables."""
        self.path_books_data = os.getenv("PATH_BOOKS_DATA", "data/books.json")
        self.path_fines_data = os.getenv("PATH_FINES_DATA", "data/fines.json")
        self.path_loans_data = os.getenv("PATH_LOANS_DATA", "data/loans.json")  
        
