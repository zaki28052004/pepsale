from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: int
    type: Literal["email", "sms", "inapp"]
    message: str

class NotificationOut(BaseModel):
    id: int
    user_id: int
    type: str
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True
