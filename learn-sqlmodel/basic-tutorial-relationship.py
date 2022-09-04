import logging
from loguru import logger
from sqlmodel import text, select
from hero.models.hero_relationship import Hero, Team
from hero.db import init_db, get_session

def create_heroes_by_relationship():
    with get_session() as session:
        session.exec(text("delete from hero"))
        session.exec(text("delete from team"))
        session.commit()

        team_avengers = Team(name="Avengers", headquarters="New York")
        team_justice = Team(name="Justice League",
                            headquarters="Washington DC")

        teams = [team_avengers, team_justice]

        heroes = [
            Hero(name="superman", secret_name="Clark Kent", age=30, team=team_justice),
            Hero(name="batman", secret_name="Bruce Wayne", age=40, team=team_justice),
            Hero(name="wonder woman", secret_name="diana princess", age=40, team=team_justice),
            Hero(name="ironman", secret_name="Tony Stark", age=50, team=team_avengers),
            Hero(name="spiderman", secret_name="Peter Parker", age=19, team=team_avengers),
            Hero(name="hulk", secret_name="Bruce Banner", age=32, team=team_avengers),
            Hero(name="wolverine", secret_name="James Howlett", age=35, team=team_avengers),
            Hero(name="thor", secret_name="Thor Odinson", age=25, team=team_avengers),
            Hero(name="captain america", secret_name="Steve Rogers", team=team_avengers),
        ]
        session.add_all(heroes)
        
        session.commit()


def create_teams_by_relationship():
    with get_session() as session:
        session.exec(text("delete from hero"))
        session.exec(text("delete from team"))
        session.commit()

        heroes = [
            Hero(name="superman", secret_name="Clark Kent",
                 age=30),
            Hero(name="batman", secret_name="Bruce Wayne",
                 age=40),
            Hero(name="wonder woman", secret_name="diana princess",
                 age=40),
            Hero(name="ironman", secret_name="Tony Stark",
                 age=50),
            Hero(name="spiderman", secret_name="Peter Parker",
                 age=19),
            Hero(name="hulk", secret_name="Bruce Banner",
                 age=32),
            Hero(name="wolverine", secret_name="James Howlett",
                 age=35),
            Hero(name="thor", secret_name="Thor Odinson",
                 age=25),
            Hero(name="captain america",
                 secret_name="Steve Rogers"),
        ]

        team_avengers = Team(name="Avengers", headquarters="New York", heroes=heroes[3:])
        team_justice = Team(name="Justice League",
                            headquarters="Washington DC", heroes=heroes[:3])

        teams = [team_avengers, team_justice]

        session.add_all(teams)

        session.commit()

def create_more_heroes():
    with get_session() as session:
        team = session.exec(select(Team).where(text("team.name ilike '%avenger%'"))).first()
        # logger.info("team of 'avenger' : {team}", team=team)
        # logger.info("member : {members}", members=team.heroes)
        team.heroes.append(Hero(name="black widow", secret_name="Natasha Romanoff"))
        session.add(team)
        session.commit()


def read_hero_with_team():
    with get_session() as session:
        hero = session.exec(select(Hero).where(Hero.name=="ironman")).first()
        logger.info("hero : {hero}", hero=hero)
        logger.info("tema : {team}", team=hero.team)

def read_team_with_heroes():
    with get_session() as session:
        team = session.exec(select(Team).where(Team.name=="Avengers")).first()
        logger.info("team : {team}", team=team)
        logger.info("members : {members}", members=team.heroes)

def remove_hero_from_team():
    with get_session() as session:
        hero = session.exec(select(Hero).where(Hero.name=="ironman")).first()
        logger.info("hero : {hero}", hero=hero)
        logger.info("tema : {team}", team=hero.team)
        hero.team = None
        session.add(hero)
        session.commit()
        
        team = session.exec(select(Team).where(Team.name=="Avengers")).first()
        logger.info("after team: {team}", team=[name for name in map(lambda x: x.name, team.heroes)])

def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    init_db(log_level=logging.DEBUG)
    # create_heroes_by_relationship()
    create_teams_by_relationship()
    create_more_heroes()
    read_hero_with_team()
    read_team_with_heroes()
    remove_hero_from_team()

if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("done")
