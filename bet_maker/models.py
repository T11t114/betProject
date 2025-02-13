from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class BetStatus(enum.Enum):
    PENDING = "pending"
    WON = "won"
    LOST = "lost"

class Bet(Base):
    __tablename__ = "bets"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    amount = Column(Float, nullable=False)
    status = Column(Enum(BetStatus), default=BetStatus.PENDING)
