from fastapi import FastAPI, HTTPException
from message_queue.queue import SimpleMessageQueue

app = FastAPI()
queue = SimpleMessageQueue()

@app.post("/publish/")
async def publish_message(message: str):
    try:
        await queue.publish(message)
        return {"status": "Message published", "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


