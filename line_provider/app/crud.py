from typing import Optional, List
from app.schemas import Event, EventState
from app.database import events


def get_event(event_id: str) -> Optional[Event]:
    """
    Получает событие по ID.
    """
    return events.get(event_id)

def get_all_events() -> List[Event]:
    """
    Возвращает список всех событий.
    """
    return list(events.values())

def get_events_by_state(state: EventState) -> List[Event]:
    """
    Возвращает список событий по заданному статусу.
    """
    return [event for event in events.values() if event.state == state]

def get_expired_events(current_time: int) -> List[Event]:
    """
    Возвращает список событий, у которых истёк дедлайн.
    """
    return [event for event in events.values() if event.deadline < current_time]

def get_fresh_events(current_time: int) -> List[Event]:
    """
    Возвращает список событий, у которых не истёк дедлайн.
    """
    return [event for event in events.values() if event.deadline > current_time]

def create_event(event: Event) -> Event:
    """
    Создаёт новое событие в имитации базы данных.
    """
    events[event.event_id] = event
    return event

def update_event_status(event_id: str, status: EventState) -> Optional[Event]:
    """
    Обновляет статус события.
    """
    event = events.get(event_id)
    if event:
        event.state = status
        event.status_updated = True
    return event

def delete_event(event_id: str) -> Optional[Event]:
    """
    Удаляет событие по ID.
    """
    return events.pop(event_id, None)


