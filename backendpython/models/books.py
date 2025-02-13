from pydantic import BaseModel


class BookDTO(BaseModel):
    title: str
    author: str
    category: str
    isbn: str
    available: bool
