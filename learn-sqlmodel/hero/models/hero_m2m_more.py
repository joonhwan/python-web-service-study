from typing import Optional, List, ForwardRef
from sqlmodel import SQLModel, Field, Relationship


class HeroTeamLink(SQLModel, table=True):
    hero_id: int | None = Field(
        default=None, primary_key=True, foreign_key="hero.id")
    team_id: int | None = Field(
        default=None, primary_key=True, foreign_key="team.id")
    is_training: bool = False

    hero: "Hero" = Relationship(back_populates="team_links")
    team: "Team" = Relationship(back_populates="hero_links")


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    # heroes: List["Hero"] = Relationship(
    #     back_populates="teams", link_model=HeroTeamLink)
    hero_links: list[HeroTeamLink] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    #
    # teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
    team_links: list[HeroTeamLink] = Relationship(back_populates="hero")

