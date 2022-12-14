from loguru import logger
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine

logger.debug("importing hero.py")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

