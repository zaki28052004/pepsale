from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models
import aio_pika
import json

router = APIRouter()

@router.post("/notifications")
async def send_notification(payload: schemas.NotificationCreate):
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps(payload.dict()).encode()),
        routing_key="notifications",
    )
    await connection.close()
    return {"status": "queued"}

@router.get("/users/{user_id}/notifications", response_model=list[schemas.NotificationOut])
def get_user_notifications(user_id: int, db: Session = Depends(database.SessionLocal)):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
