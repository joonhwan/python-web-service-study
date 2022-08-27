from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel
from sqlmodel import Session

DB_URL="postgresql+asyncpg://postgres:postgres@localhost:15432"
engine = create_async_engine(f"{DB_URL}/hero")

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session_async():
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session
