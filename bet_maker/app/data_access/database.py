from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import config



def new_session_maker() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        config.postgres_.DATABASE_URL,
    )

    return async_sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session_maker = new_session_maker()
    async with session_maker() as session:
        yield session