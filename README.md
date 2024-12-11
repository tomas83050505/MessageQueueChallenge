# Message Queue Challenge Solution

## Overview
This project implements an asynchronous message queue library along with two FastAPI microservices. The library supports publishing, subscribing, and retrying messages. The microservices demonstrate the library's functionality, including HTTP-based publishing and WebSocket-based real-time communication.

---

## Features
- Lightweight and modular message queue library (`SimpleMessageQueue`).
- Supports:
  - **Publishing**: Add messages to the queue.
  - **Subscribing**: Process messages asynchronously.
  - **Retry Logic**: Handle failures when publishing messages.
- Two FastAPI microservices:
  - **Service A**: Publishes messages via an HTTP API.
  - **Service B**: Processes messages and supports WebSocket communication.
- Automated testing with `pytest` and `pytest-asyncio`.
- Simple setup and execution using a `setup_and_run.py` script.

---

## Requirements
- Python 3.8 or higher
- Pip (Python package manager)

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/tomas83050505/MessageQueueChallenge.git>
   cd MessageQueueChallenge
