from pydantic import BaseModel

# Data Transfer Object (DTO)
class NotificationDTO(BaseModel):
    user_id: str
    message: str
    timestamp: str
    read: bool
