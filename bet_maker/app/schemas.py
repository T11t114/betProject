import enum

from pydantic import BaseModel

class BetState(enum.IntEnum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3

class BetSchema(BaseModel):
    event_id: str
    amount: float


class BetResponse(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True 