from typing import List
from fastapi import APIRouter
from models.notifications import NotificationDTO
from services.notifications_service import NotificationService

router = APIRouter()
service = NotificationService()

@router.get("/notifications/all", response_model=List[NotificationDTO])
def get_all_notifications():
    return service.get_all()

@router.get("/notifications/user/{user_id}", response_model=List[NotificationDTO])
def get_notifications_by_user(user_id: str):
    return service.get_by_user(user_id)

@router.post("/notifications/add")
def add_notification(notification: NotificationDTO):
    service.add_notification(notification)
    return {"message": "Notification added successfully"}

@router.put("/notifications/read/{user_id}")
def mark_as_read(user_id: str):
    service.mark_as_read(user_id)
    return {"message": "Notifications marked as read"}
