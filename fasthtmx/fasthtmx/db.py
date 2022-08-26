import os
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DB_URL = os.environ.get("DB_URL") 
# DB_URL = DB_URL or "postgresql+psycopg2://postgres:postgres@localhost:15432/fasthtmx"

# engine = create_engine(DB_URL, echo=True)

# def init_db():
#     SQLModel.metadata.create_all(engine)

# def close_db():
#     engine.dispose()

# def new_session():
#     return Session(engine)

# def get_session():
#     with Session(engine) as session:
#         yield session

DB_URL = DB_URL or "postgresql+asyncpg://postgres:postgres@localhost:15432/fasthtmx"
engine = create_async_engine(DB_URL, echo=True)

async def init_db_async():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session_async():
    async_sesion =sessionmaker(
        engine, 
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_sesion() as session:
        yield session
    