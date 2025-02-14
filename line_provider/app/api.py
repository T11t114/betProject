import datetime
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from line_provider.app.producer import handle_event_status
from line_provider.app.schemas import Event, EventState
from line_provider.app import dependencies
import time

 
router = APIRouter()


@router.get("/", tags=["Events"])
async def get_events(
    usecase: callable = Depends(dependencies.get_get_all_events)
):
    """
    Возвращает список всех событий
    """
    return usecase()

@router.get("/state", tags=["Events"])
async def get_events_by_state(
    state: EventState,
    usecase: callable = Depends(dependencies.get_get_events_by_state)
):
    """
    Возвращает список событий с указанным статусом.
    """
    return usecase(state)  


@router.get("/expired", tags=["Events"])
async def get_expired_events(
    usecase: callable = Depends(dependencies.get_get_expired_events)
):
    """
    Возвращает список просроченных событий.
    """
    return usecase(int(time.time()))

@router.get("/fresh", tags=["Events"])
async def get_fresh_events(
    usecase: callable = Depends(dependencies.get_get_fresh_events)
):
    """
    Возвращает список не просроченных событий.
    """
    return usecase(int(time.time()))

@router.post("/event", tags=["Admin Panel"])
async def create_event(
    event: Event,
    usecase: callable = Depends(dependencies.get_create_event)
):
    """
    Создаёт новое событие или обновляет его, если событие с таким ID уже существует.
    """
    event.deadline += int(time.time())
    result = usecase(event)
    return {"message": "Event created successfully", "event": result}


@router.delete("/{event_id}", tags=["Admin Panel"])
async def delete_event(
    event_id: str,
    usecase: callable = Depends(dependencies.get_delete_event)
):
    """
    Удаляет событие по ID.
    """
    result = usecase(event_id)
    if result:
        return {"message": "Event deleted successfully", "event": result}
    raise HTTPException(status_code=404, detail="Event not found")


@router.put("/{event_id}/status", tags=["Admin Panel"])
async def update_event_status(
    event_id: str,
    status: EventState,
    usecase: callable = Depends(dependencies.get_update_event_status)
):
    """
    Обновляет статус события по ID.
    """
    result = usecase(event_id, status)
    if result:
        await handle_event_status(event_id, status)
        return {"message": "Event status updated successfully", "event": result}
    raise HTTPException(status_code=404, detail="Event not found")


@router.get("/{event_id}", tags=["Events"])
async def get_event(
    event_id: str = Path(...),
    usecase: callable = Depends(dependencies.get_get_event)
):
    """
    Получает событие по ID.
    """
    result = usecase(event_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Event not found")
