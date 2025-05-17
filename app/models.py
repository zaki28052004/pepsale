from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    type = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
