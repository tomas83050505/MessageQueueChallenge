
import asyncio

class SimpleMessageQueue:
    def __init__(self, max_size=100):
        self.queue = asyncio.Queue(maxsize=max_size)

    async def publish(self, message):
        """Adds a message to the queue."""
        try:
            await self.queue.put(message)
            print(f"Message published: {message}")
        except asyncio.QueueFull:
            print("Queue is full. Failed to publish message.")

    async def subscribe(self, handler):
        """Processes messages using the provided handler function."""
        while True:
            try:
                message = await self.queue.get()
                await handler(message)
                self.queue.task_done()
            except Exception as e:
                print(f"Error while processing message: {e}")

    async def retry_publish(self, message, retries=3, delay=1):
        """Retries publishing a message."""
        for attempt in range(retries):
            try:
                await self.publish(message)
                return
            except Exception as e:
                print(f"Retry {attempt + 1}/{retries} failed: {e}")
                await asyncio.sleep(delay)
        print(f"Failed to publish message after {retries} retries.")




