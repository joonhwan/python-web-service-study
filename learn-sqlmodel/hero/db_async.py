import logging
from typing import Callable
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from hero.util.logging import configure_log_handler

DB_URL = "postgresql+asyncpg://postgres:postgres@localhost:15432"
engine = create_async_engine(f"{DB_URL}/hero")


async def init_db(*, log_level=logging.WARNING):
    configure_log_handler(log_level=log_level)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# def get_session():
#     return AsyncSession(engine)

async_session: Callable[[], AsyncSession] = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session():
    session: AsyncSession = async_session()
    async with session:
        yield session
