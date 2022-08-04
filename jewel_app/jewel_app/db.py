from sqlmodel import SQLModel, create_engine, Session
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

db_url = "sqlite:///gem.db"
engine = create_engine(db_url, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

