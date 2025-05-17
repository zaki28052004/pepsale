# Notification Service

## Overview
A notification service built with FastAPI, SQLite, and RabbitMQ that supports Email, SMS, and In-App notifications.

## Features
- API to send and fetch notifications
- Email, SMS, and In-App notification support
- Asynchronous processing using RabbitMQ
- SQLite database for storing In-App notifications

## Setup

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Run RabbitMQ** (if not installed locally):
```bash
docker run -d --hostname rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

3. **Start FastAPI server**
```bash
uvicorn app.main:app --reload
```

4. **Run the consumer**
```bash
python app/workers/consumer.py
```

## API Endpoints

- `POST /notifications` – Send a notification
- `GET /users/{id}/notifications` – Get all in-app notifications for a user
