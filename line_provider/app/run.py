from fastapi import FastAPI
from line_provider.app.producer import producer
from line_provider.app.api import router as events_router

# uvicorn line_provider.app.run:app --reload --port 8002

 
app = FastAPI(
    title="Sports Betting API",
    description="API for managing sports betting events",
    version="0.1"
)

app.include_router(events_router, prefix="/events")


@app.on_event("startup")
async def startup_event():
    """Start up event for FastAPI application."""
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event for FastAPI application."""
    await producer.stop()