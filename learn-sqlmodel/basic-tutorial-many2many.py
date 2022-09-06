import logging
from loguru import logger
from sqlmodel import text, select
from hero.models.hero_m2m import Hero, Team
from hero.db import init_db, get_session


def create_heroes_by_relationship():
    with get_session() as session:
        session.exec(text("delete from heroteamlink"))
        session.exec(text("delete from hero"))
        session.exec(text("delete from team"))
        session.commit()

        team_avengers = Team(name="Avengers", headquarters="New York")
        team_justice = Team(name="Justice League",
                            headquarters="Washington DC")

        teams = [team_avengers, team_justice]

        heroes = [
            Hero(name="superman", secret_name="Clark Kent",
                 age=30, teams=[team_justice, team_avengers]),
            Hero(name="batman", secret_name="Bruce Wayne",
                 age=40, teams=[team_justice]),
            Hero(name="wonder woman", secret_name="diana princess",
                 age=40, teams=[team_justice]),
            Hero(name="ironman", secret_name="Tony Stark",
                 age=50, teams=[team_avengers]),
            Hero(name="spiderman", secret_name="Peter Parker",
                 age=19, teams=[team_avengers]),
            Hero(name="hulk", secret_name="Bruce Banner",
                 age=32, teams=[team_avengers]),
            Hero(name="wolverine", secret_name="James Howlett",
                 age=35, teams=[team_avengers, team_justice]),
            Hero(name="thor", secret_name="Thor Odinson",
                 age=25, teams=[team_avengers]),
            Hero(name="captain america",
                 secret_name="Steve Rogers", teams=[team_avengers]),
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

        team_avengers = Team(
            name="Avengers", headquarters="New York",
            heroes=heroes[3:]
        )
        team_justice = Team(name="Justice League",
                            headquarters="Washington DC", heroes=heroes[:5])

        teams = [team_avengers, team_justice]

        session.add_all(teams)

        session.commit()


def create_more_heroes():
    with get_session() as session:
        team = session.exec(select(Team).where(
            text("team.name ilike '%avenger%'"))).first()
        # logger.info("team of 'avenger' : {team}", teams=[team])
        # logger.info("member : {members}", members=team.heroes)
        team.heroes.append(
            Hero(name="black widow", secret_name="Natasha Romanoff")
        )
        session.add(team)
        session.commit()

def read_teams_with_heroes():
     logger.info("📜 read teams with heroes")
     with get_session() as session:
          teams = session.exec(select(Team)).all()
          heroes = session.exec(select(Hero)).all()
          for team in teams:
               logger.info("team : {team}", team=team)
               # for hero in team.heroes:
               #      logger.info("   - {hero}", hero=hero)
          for hero in heroes:
               logger.info("hero: {hero}", hero=hero)

          for team in teams:
               logger.warning("team : {team}", team=team)
               for hero in team.heroes:
                    logger.info("team : {team} - {hero}", team=team, hero=hero)

def wolverine_leave_team():
     logger.info("📜 wolverine 이 avengers를 떠납니다")
     with get_session() as session:
          hero = session.exec(select(Hero).where(Hero.name == "wolverine")).first()
          avengers = next((t for t in hero.teams if t.name == "Avengers"), None)
          hero.teams.remove(avengers)
          session.add(hero)
          session.commit()
     
     with get_session() as session:
          heroes = session.exec(select(Hero)).all()
          for hero in heroes:
               logger.info("hero: {hero}", hero=hero)


def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    init_db(log_level=logging.INFO)
    create_heroes_by_relationship()
    create_more_heroes()
    read_teams_with_heroes()
    wolverine_leave_team()


if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("done")
