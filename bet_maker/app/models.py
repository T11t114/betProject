from sqlalchemy import Column, Integer, Float, Enum, String
from sqlalchemy.orm import DeclarativeBase

from bet_maker.app.schemas import BetState


class Base(DeclarativeBase):
    pass

class Bet(Base):
    __tablename__ = "bets"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String)
    amount = Column(Float, nullable=False)
    status = Column(Enum(BetState), default=BetState.NEW)
