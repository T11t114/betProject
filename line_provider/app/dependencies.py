from app import crud


def get_create_event() -> callable:
    return crud.create_event

def get_get_event() -> callable:
    return crud.get_event

def get_get_all_events() -> callable:
    return crud.get_all_events

def get_delete_event() -> callable:
    return crud.delete_event

def get_get_events_by_state() -> callable:
    return crud.get_events_by_state

def get_get_expired_events() -> callable:
    return crud.get_expired_events

def get_get_fresh_events() -> callable:
    return crud.get_fresh_events

def get_update_event_status() -> callable:
    return crud.update_event_status