import logging
from loguru import logger
from sqlmodel import text, select
from hero.models import Hero
from hero.db import init_db, get_session
from hero.models.hero import Team

def create_heroes_by_id():
    with get_session() as session:
        session.exec(text("delete from hero"))
        session.exec(text("delete from team"))
        session.commit()

        team_avengers = Team(name="Avengers", headquarters="New York")
        team_justice = Team(name="Justice League",
                            headquarters="Washington DC")
        teams = [
            team_avengers,
            team_justice
        ]
        session.add_all(teams)
        session.commit()
        
        for team in teams:
            session.refresh(team)
            logger.info(team)

        heroes = [
            Hero(name="superman", secret_name="Clark Kent", age=30, team_id=team_justice.id),
            Hero(name="batman", secret_name="Bruce Wayne", age=40, team_id=team_justice.id),
            Hero(name="wonder woman", secret_name="diana princess", age=40, team_id=team_justice.id),
            Hero(name="ironman", secret_name="Tony Stark", age=50, team_id=team_avengers.id),
            Hero(name="spiderman", secret_name="Peter Parker", age=19, team_id=team_avengers.id),
            Hero(name="hulk", secret_name="Bruce Banner", age=32, team_id=team_avengers.id),
            Hero(name="wolverine", secret_name="James Howlett", age=35, team_id=team_avengers.id),
            Hero(name="thor", secret_name="Thor Odinson", age=25, team_id=team_avengers.id),
            Hero(name="captain america", secret_name="Steve Rogers", team_id=team_avengers.id),
        ]
        session.add_all(heroes)
        session.commit()


def read_heroes_and_team_by_id():
    with get_session() as session:
        logger.info("✔︎ join 테스트 하기 ")
        # q = select(Hero).join(Team).where(Team.name.contains("Avenger"))
        q = select(Hero, Team).join(Team).where(text("team.name ilike '%avenger%'"))
        r = session.exec(q)
        for hero in r:
            # hero.name, hero.age, hero.team_id
            logger.info(hero)


def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    init_db(log_level=logging.DEBUG)
    create_heroes_by_id()
    read_heroes_and_team_by_id()

if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("done")
