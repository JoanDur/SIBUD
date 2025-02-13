import pytest
from backendpython.models.notifications import NotificationDTO
from backendpython.services.notifications_service import NotificationService
from datetime import datetime

@pytest.fixture
def notification_service():
    return NotificationService()

def test_add_notification(notification_service):
    notification = NotificationDTO(user_id="1", message="Test Notification", timestamp=str(datetime.now()), read=False)
    notification_service.add_notification(notification)
    notifications = notification_service.get_by_user("1")
    assert any(n.message == "Test Notification" for n in notifications)

def test_mark_as_read(notification_service):
    notification_service.mark_as_read("1")
    notifications = notification_service.get_by_user("1")
    assert all(n.read for n in notifications)
