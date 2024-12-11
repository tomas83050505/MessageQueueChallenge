from fastapi import FastAPI, WebSocket
from message_queue.queue import SimpleMessageQueue

app = FastAPI()
queue = SimpleMessageQueue()

@app.on_event("startup")
async def start_subscriber():
    """Starts the subscriber to process messages."""
    async def process_message(message):
        print(f"Processing message: {message}")

    import asyncio
    asyncio.create_task(queue.subscribe(process_message))

@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            await queue.publish(data)
            await websocket.send_text(f"Received: {data}")
        except Exception as e:
            await websocket.send_text(f"Error: {str(e)}")
