import pytest
import httpx
from app.main import app
from app.schemas import EventState


@pytest.mark.asyncio
async def test_create_event():
    """
    Тест для создания нового события.
    """
    event_data = {
        "event_id": "1",
        "name": "Test Event",
        "state": EventState.NEW,
        "coefficient": 1.5,
        "deadline": 1712345678
    }
    async with httpx.AsyncClient(app=app, base_url='http://localhost') as client:
        response = await client.post("/event", json=event_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Event created successfully"

@pytest.mark.asyncio
async def test_get_event():
    """
    Тест для получения события по ID.
    """
    async with httpx.AsyncClient(app=app, base_url='http://localhost') as client:
        response = await client.get("/event/1")
    assert response.status_code == 200
    assert response.json()["event_id"] == "1"

@pytest.mark.asyncio
async def test_get_events():
    """
    Тест для получения списка всех событий.
    """
    async with httpx.AsyncClient(app=app, base_url='http://localhost') as client:
        response = await client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_events_by_state():
    """
    Тест для получения событий с определённым статусом.
    """
    async with httpx.AsyncClient(app=app, base_url='http://localhost') as client:
        response = await client.get("/events/state?state=1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_delete_event():
    """
    Тест для удаления события по ID.
    """
    async with httpx.AsyncClient(app=app, base_url='http://localhost') as client:
        response = await client.delete("/event/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Event deleted successfully"
