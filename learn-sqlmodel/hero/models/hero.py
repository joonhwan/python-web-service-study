from typing import Optional
from sqlmodel import SQLModel, Field
from loguru import logger

logger.error("π³π³π³π³π³π³ μΌμ π³π³π³π³π³π³")

# tabl = True μΈ ν΄λμ€λ§ SQLModel.metatdata μ λ±λ‘λλ©°,
# tabl = False μΈ ν΄λμ€λ SQLModel.metatdata μ λ±λ‘λμ§ μμ.
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str 
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str