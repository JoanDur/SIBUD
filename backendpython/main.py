"""Main module of the SIBUD project incluye los routers de cada modulo

Author: Joan Sebastian Duran Pradilla
"""

from fastapi import FastAPI
from controllers import books_router, fines_router, loans_router, notifications_router

app = FastAPI(
    title="SIBUD - Library Management System",
    description="API REST para la gestión de préstamos de libros en SIBUD.",
    version="1.0.0",
)


app.include_router(books_router.router, prefix="/books", tags=["Books"])
app.include_router(loans_router.router, prefix="/loans", tags=["Loans"])
app.include_router(fines_router.router, prefix="/fines", tags=["Fines"])
app.include_router(notifications_router.router, prefix="/notifications", tags=["Notifications"])

@app.get("/")
def root():
    """ver que sirve"""
    return {"message": "Bienvenido a SIBUD - Sistema de Bibliotecas"}