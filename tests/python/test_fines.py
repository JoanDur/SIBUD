import pytest
from backendpython.models.fines import FineDTO
from backendpython.services.fines_service import FineService
from datetime import datetime

@pytest.fixture
def fine_service():
    return FineService()

def test_add_fine(fine_service):
    fine = FineDTO(user_id="1", amount=10.0, due_date=str(datetime.now()), paid=False)
    fine_service.add_fine(fine)
    fines = fine_service.get_all_fines()
    assert any(f.user_id == "1" and f.amount == 10.0 for f in fines)

def test_pay_fine(fine_service):
    fine_service.pay_fine("1")
    fines = fine_service.get_all_fines()
    assert all(f.paid for f in fines if f.user_id == "1")
