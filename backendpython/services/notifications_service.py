from typing import List
from models.notifications import NotificationDTO
from repositories.notifications_repository import NotificationRepository

class NotificationService:
    def __init__(self):
        self.repository = NotificationRepository()
    
    def get_all(self) -> List[NotificationDTO]:
        return self.repository.get_all_notifications()
    
    def get_by_user(self, user_id: str) -> List[NotificationDTO]:
        return self.repository.get_notifications_by_user(user_id)
    
    def add_notification(self, notification: NotificationDTO):
        self.repository.add_notification(notification)
    
    def mark_as_read(self, user_id: str):
        self.repository.mark_as_read(user_id)
