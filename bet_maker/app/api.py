import httpx
from fastapi import APIRouter, Depends, HTTPException
from app import  dependencies
from app.data_access.database import get_session
from app.schemas import BetResponse, BetSchema
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

async def fetch_events():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("http://lineprovider:8002/events/fresh")
            response.raise_for_status()  
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch events from line-provider")


@router.get("/events")
async def get_available_events():
    events = await fetch_events()
    return events


@router.post("/bets")
async def get_bets(
    session: AsyncSession = Depends(get_session),
    usecase: callable = Depends(dependencies.get_get_bets)) -> list[BetResponse]:
    bets = await usecase(session)
    return [BetResponse.from_orm(bet) for bet in bets]


@router.post("/bet")
async def create_bet(
    data: BetSchema,
    session: AsyncSession = Depends(get_session),
    usecase: callable = Depends(dependencies.get_create_bet),
    ):
    bet = await usecase(data, session)
    return bet 
