import pytest
import asyncio

import sys
import os


# Add the root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))



from message_queue.queue import SimpleMessageQueue

@pytest.mark.asyncio
async def test_publish_and_subscribe():
    queue = SimpleMessageQueue()
    results = []

    async def handler(message):
        results.append(message)

    asyncio.create_task(queue.subscribe(handler))
    await queue.publish("Test message")
    await asyncio.sleep(0.1)

    assert results == ["Test message"]

@pytest.mark.asyncio
async def test_retry_publish():
    queue = SimpleMessageQueue()
    await queue.retry_publish("Retry message", retries=2, delay=0.1)
    assert queue.queue.qsize() == 1

