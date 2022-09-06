import logging
from loguru import logger
from sqlmodel import text, select
from hero.models.hero_m2m_more import Hero, Team, HeroTeamLink
from hero.db import init_db, get_session


def create_heroes_by_link():
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
                 age=30),
            Hero(name="batman", secret_name="Bruce Wayne", age=40),
            Hero(name="wonder woman", secret_name="diana princess", age=40),
        ]

        links = [
          HeroTeamLink(team=team_avengers, hero=heroes[0]),
          HeroTeamLink(team=team_justice, hero=heroes[1]),
          HeroTeamLink(team=team_justice, hero=heroes[2]),
        ]
        session.add_all(links)

        session.commit()


def create_more_heroes():
    with get_session() as session:
        team = session.exec(select(Team).where(text("team.name ilike '%avenger%'"))).first()        # logger.info("team of 'avenger' : {team}"])
        # logger.info("member : {members}", members=team.heroes)
        session.add_all([
          HeroTeamLink(team=team, hero=Hero(name="wolverine", secret_name="logan", age=40)),
          HeroTeamLink(team=team, hero=Hero(name="hulk", secret_name="bruce banner", age=40)),
        ])
        session.commit()

def read_heroes():
     logger.info("📄 hero 와 참가 team 조회")
     with get_session() as session:
          heroes = session.exec(select(Hero)).all()
          for hero in heroes:
               logger.info("hero : {hero}", hero=hero)
               for link in hero.team_links:
                    logger.info(" - {link}", link=link)

def update_traning_state():
     with get_session() as session:
          w_heros = session.exec(select(Hero).where(Hero.name.startswith("w"))).all()
          for hero in w_heros:
               for link in hero.team_links:
                    link.is_training = True
          session.commit()

def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    init_db(log_level=logging.WARNING)
    create_heroes_by_link()
    create_more_heroes()
    read_heroes()
    update_traning_state()
    read_heroes()
#     read_teams_with_heroes()
#     wolverine_leave_team()


if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("done")
