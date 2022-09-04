import sys
from loguru import logger
from sqlmodel import select, or_, text
from hero.models import Hero
from hero.db import init_db, get_session

def delete_heroes():
    with get_session() as session:
        session.execute(text("DELETE FROM hero"))
        session.commit()


def create_heroes():
    heroes = [
        Hero(name="superman", secret_name="Clark Kent", age=30),
        Hero(name="batman", secret_name="Bruce Wayne", age=40),
        Hero(name="ironman", secret_name="Tony Stark", age=50),
        Hero(name="spiderman", secret_name="Peter Parker", age=19),
        Hero(name="hulk", secret_name="Bruce Banner", age=32),
        Hero(name="wolverine", secret_name="James Howlett", age=35),
        Hero(name="thor", secret_name="Thor Odinson", age=25),
        Hero(name="captain america", secret_name="Steve Rogers"),
    ]

    with get_session() as session:
        for hero in heroes:
            session.add(hero)
        session.commit()

def update_heroes():
    logger.info("🚀 ------------- update() ----------------- ")
    with get_session() as session:
        q = select(Hero).where(Hero.name == "superman")
        results = session.exec(q)
        hero = results.one()
        logger.info("before set age,  hero : {hero}", hero=hero)
        hero.age = hero.age + 1
        logger.info("after set age,  hero : {hero}", hero=hero)
        session.commit()

def update_heroes_by_add():
    logger.info("🚀 ------------- update by add() ----------------- ")
    with get_session() as session:
        q = select(Hero).where(Hero.name == "superman")
        results = session.exec(q)
        hero = results.one()
        logger.info("before set age,  hero : {hero}", hero=hero)
        hero.age = hero.age + 1
        session.add(hero)
        session.commit()
        logger.info("update by add 한 후 : {hero}", hero=hero)
        logger.info("refresh hero")
        session.refresh(hero)
        logger.info(hero)


    logger.info("🚀 ------------- update by add -> check  ----------------- ")
    with get_session() as session:
        q = select(Hero).where(Hero.name == "superman")
        results = session.exec(q)
        hero = results.one()
        logger.info("check superman  hero : {hero}", hero=hero)

def update_multiple_heroes():
    with get_session() as session:
        logger.info("get heroes with age > 30")
        q = select(Hero).where(Hero.age > 30)
        results = session.exec(q)
        heroes = results.all()
        logger.info("result : {heroes}", heroes=heroes)

        logger.info("updating age + 1")
        for hero in heroes:
            hero.age = hero.age + 1
            session.add(hero)
        session.commit()

        logger.info("refresh multiple heroes")
        for hero in heroes:
            session.refresh(hero)
        

def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    import logging
    init_db(log_level=logging.INFO)
    # delete_heroes()
    # create_heroes()
    # update_heroes()
    # update_heroes_by_add()
    update_multiple_heroes()


if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("Done")
