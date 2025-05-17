from ..models import Notification
from ..database import SessionLocal

async def save_inapp_notification(user_id: int, message: str):
    db = SessionLocal()
    notif = Notification(user_id=user_id, type="inapp", message=message)
    db.add(notif)
    db.commit()
    db.close()
