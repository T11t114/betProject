import asyncio
from fastapi import FastAPI
from app.api import router
from app.consumer import consumer, consume

# uvicorn bet_maker.app.run:app --reload --port 8003

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    await consumer.start()
    task = asyncio.create_task(consume())


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""
    await consumer.stop()