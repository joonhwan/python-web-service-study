from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


# tabl = True 인 클래스만 SQLModel.metatdata 에 등록되며,
# tabl = False 인 클래스는 SQLModel.metatdata 에 등록되지 않음.
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str 
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    # 
    team: Optional["Team"] = Relationship(back_populates="heroes")
    

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    # 
    heroes: list[Hero] | None = Relationship(back_populates="team")

