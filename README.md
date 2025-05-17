# 📨 Notification Service

A microservice-based notification system built with **FastAPI** and **RabbitMQ** to send **email**, **SMS**, and **in-app notifications**. Designed for scalable delivery and background processing using message queues.

---

## 🚀 Features

- 🔁 Asynchronous Notification Handling via RabbitMQ
- 📬 Notification Types: `email`, `sms`, and `in_app`
- 🧾 SQLite storage for in-app messages
- ⚡ FastAPI-powered RESTful APIs with Swagger Docs
- 👨‍🔧 Background consumer to process queued notifications
- ✅ Easy to extend with real email/SMS APIs (SendGrid, Twilio)

---

## 📦 Tech Stack

- **Python 3.11+**
- **FastAPI** – Web framework
- **RabbitMQ** – Queue for background processing
- **SQLite** – Lightweight DB for storing in-app notifications
- **Pydantic** – Request validation
- **Uvicorn** – ASGI server

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/zaki28052004/pepsale.git
cd pepsale
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
