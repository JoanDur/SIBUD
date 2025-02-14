import pytest
from backendpython.models.fines import FineDTO
from backendpython.services.fines_service import FineService
from datetime import datetime

@pytest.fixture
def fine_service():
    service = FineService()
    service.clear_fines()  # Limpia multas antes de cada test
    return service

def test_add_fine(fine_service):
    fine = FineDTO(user_id="1", loan_id="1", reason="Overdue", fine_date=str(datetime.now()), amount=10.0, due_date=str(datetime.now()), paid=False)
    fine_service.add_fine(fine)
    fines = fine_service.get_all()
    assert fines is not None
    assert any(f.user_id == "1" and f.amount == 10.0 for f in fines)

def test_mark_as_paid(fine_service):
    fine_service.add_fine(FineDTO(user_id="1", loan_id="1", reason="Overdue", fine_date=str(datetime.now()), amount=10.0, due_date=str(datetime.now()), paid=False))
    fine_service.add_fine(FineDTO(user_id="2", loan_id="1", reason="Overdue", fine_date=str(datetime.now()), amount=15.0, due_date=str(datetime.now()), paid=False))

    fine_service.mark_as_paid("1")
    
    fines = fine_service.get_all()
    
    assert fines is not None
    for f in fines:
        print(f"Multa después de marcar como pagada: {f}")  # Depuración
    
    assert all(f.paid for f in fines if f.loan_id == "1")
