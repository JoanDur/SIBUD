import json
from typing import List
from models.notifications import NotificationDTO
from environment_variables import EnvironmentVariables

class NotificationRepository:
    def __init__(self):
        env = EnvironmentVariables()
        self.path_file = env.path_notifications_data
        self._load_data()
    
    def _load_data(self):
        try:
            with open(self.path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []
    
    def get_all_notifications(self) -> List[NotificationDTO]:
        return [NotificationDTO(**notif) for notif in self.data]
    
    def get_notifications_by_user(self, user_id: str) -> List[NotificationDTO]:
        return [NotificationDTO(**notif) for notif in self.data if notif["user_id"] == user_id]
    
    def add_notification(self, notification: NotificationDTO):
        self.data.append(notification.dict())
        self._save_data()
    
    def mark_as_read(self, user_id: str):
        for notif in self.data:
            if notif["user_id"] == user_id and not notif["read"]:
                notif["read"] = True
        self._save_data()
    
    def _save_data(self):
        with open(self.path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
