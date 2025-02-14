from sqlalchemy import select
from bet_maker.app.models import Bet
from bet_maker.app.schemas import BetSchema, BetState
from sqlalchemy.ext.asyncio import AsyncSession


async def create_bet(bet: BetSchema, session: AsyncSession) -> Bet:
    db_bet = Bet(event_id=bet.event_id, amount=bet.amount)
    session.add(db_bet)
    await session.commit() 
    await session.refresh(db_bet) 
    return db_bet

async def get_all_bets(session: AsyncSession) -> list[Bet]:
    result = await session.execute(select(Bet.id, Bet.status)) 
    bets = result.all()
    return bets

async def update_bet_status(session: AsyncSession, event_id: str, status: BetState):
    result = await session.execute(select(Bet).where(Bet.event_id == event_id))
    bets = result.scalars().all()

    for bet in bets:
        bet.status = status
        session.add(bet)

    await session.commit()

