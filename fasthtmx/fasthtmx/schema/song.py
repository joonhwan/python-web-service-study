from typing import Optional
from sqlmodel import SQLModel, Field


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None

# vm
class SongCreate(SongBase):
    pass


class Song(SongBase, table=True):
    id: int = Field(primary_key=True)


