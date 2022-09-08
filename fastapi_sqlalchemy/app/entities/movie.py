from enum import unique
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import text
from app.db.env import Base, Session

class MovieEntity(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    director = Column(String)
