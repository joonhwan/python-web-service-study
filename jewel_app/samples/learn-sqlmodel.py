from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
from sqlmodel.sql.expression import SelectOfScalar

SelectOfScalar.inherit_cache = True


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


engine = create_engine("sqlite:///database.db", echo=False)


def create_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(
            name="Preventers", headquarters="Sharp Tower"
        )
        team_z_force = Team(
            name="Z-Force", headquarters="Sister Margaret’s Bar"
        )
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            team_id=team_z_force.id
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(
            name="Spider-Boy",
            secret_name="Pedro Parqueador"
        )
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()


def select_heroes():
    with Session(engine) as session:
        sql = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(sql)
        for hero, team in results:
            print(f"-- Hero: {hero},  Team: {team}")


def select_heroes_with_age():
    with Session(engine) as session:
        sql = select(Hero).where(Hero.age == 30)
        heroes = session.exec(sql)
        for hero in heroes:
            print(f"-- {hero}")


def select_heroes_paged():
    with Session(engine) as session:
        sql = select(Hero).where(Hero.age > 32).limit(2).offset(2)
        heroes = session.exec(sql)
        for hero in heroes:
            print(f"-- {hero}")


def update_heroes():
    with Session(engine) as session:
        hero = session.get(Hero, 1)
        # UPDATE
        hero.age = hero.age + 1
        session.add(hero)
        print(f' before commit) {hero}')
        session.commit()
        print(f' after commit) {hero}')
        session.refresh(hero)
        print(f' after refresh) {hero}')


def delete_hero():
    with Session(engine) as session:
        hero = session.get(Hero, 1)
        if hero:
            session.delete(hero)
            session.commit()
            print(hero)


if __name__ == "__main__":
    create_db_and_tables()
    create_heroes()
    select_heroes()
    # select_heroes_with_age()
    # select_heroes_paged()
    # update_heroes()
    # delete_hero()

    # with Session(engine) as session:
    #     statement = select(Hero).where(Hero.name == "Hero3")
    #     hero = session.exec(statement).first()
    #     print(hero)
    print("😅 Done!")
