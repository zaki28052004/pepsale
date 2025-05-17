import asyncio
import aio_pika
import json
from app.services.email import send_email
from app.services.sms import send_sms
from app.services.inapp import save_inapp_notification

async def handle_notification(message: aio_pika.IncomingMessage):
    async with message.process():
        data = json.loads(message.body.decode())
        user_id = data["user_id"]
        msg = data["message"]
        notif_type = data["type"]

        if notif_type == "email":
            await send_email(user_id, msg)
        elif notif_type == "sms":
            await send_sms(user_id, msg)
        elif notif_type == "inapp":
            await save_inapp_notification(user_id, msg)

async def main():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("notifications", durable=True)
    await queue.consume(handle_notification)
    print("Consumer started")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
