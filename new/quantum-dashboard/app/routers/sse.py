from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse  # Only this import!
import asyncio

router = APIRouter(prefix="/sse", tags=["sse"])

subscribers = set()

async def event_generator():
    queue = asyncio.Queue()
    subscribers.add(queue)
    try:
        while True:
            data = await queue.get()
            yield f"data: {data}\n\n"
    finally:
        subscribers.remove(queue)

@router.get("/stream")
async def stream(request: Request):
    return EventSourceResponse(event_generator())

# Utility to broadcast to all subscribers
async def broadcast_sse(data: str):
    for queue in list(subscribers):
        await queue.put(data)