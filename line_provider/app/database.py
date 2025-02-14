from app.schemas import Event, EventState
import time 


events: dict[str, Event] = {
    '1': Event(event_id='1', coefficient=1.20, deadline=int(time.time()) + 600, state=EventState.NEW),
    '2': Event(event_id='2', coefficient=1.15, deadline=int(time.time()) + 60, state=EventState.NEW),
    '3': Event(event_id='3', coefficient=1.67, deadline=int(time.time()) + 90, state=EventState.NEW)
}


