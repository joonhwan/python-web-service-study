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


def read_heroes():
    with get_session() as session:
        logger.warning("🚀 ------------- one() ----------------- ")
        result = session.exec(select(Hero).where(Hero.name == "superman"))
        one_hero = result.one()
        logger.info('First Hero : {hero}', hero=one_hero)

        logger.warning("🚀 ------------- one() ERROR ----------------- ")
        result = session.exec(select(Hero).where(
            Hero.age > 30).where(Hero.age < 50))
        try:
            one_hero = result.one()
        except Exception as e:
            logger.error(e)

        logger.warning("🚀 ------------- all() ----------------- ")
        result = session.exec(
            select(Hero).where(
                Hero.age > 30
            ).where(
                Hero.age < 50
            )
        )
        heroes = result.all()
        for hero in heroes:
            logger.info("{hero} {type}", hero=hero, type=type(hero))

        logger.warning("🚀 ------------- first() ----------------- ")
        result = session.exec(select(Hero).where(or_(Hero.age < 5)))
        first_hero = result.first()
        logger.info('First Hero : {hero}', hero=first_hero)

        logger.warning("🚀 ------------- get() ----------------- ")
        get_hero = session.get(Hero, one_hero.id)
        logger.info('get() Hero : {hero}', hero=get_hero)


def read_heroes_paged():
    with get_session() as session:
        logger.warning("🚀 ------------- paged() ----------------- ")
        page_index = 0
        page_size = 3
        while True:
            q = select(Hero).offset(page_index * page_size).limit(page_size)
            result = session.exec(q)
            heroes = result.all()
            logger.info("📖 Page: {page_index} (count={count})", page_index=page_index, count=len(heroes))
            for hero in heroes:
                logger.info("{hero} {type}", hero=hero, type=type(hero))
            if len(heroes) < page_size:
                break
            page_index += 1


def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    import logging
    init_db(log_level=logging.INFO)
    # delete_heroes()
    # create_heroes()
    # read_heroes()
    read_heroes_paged()


if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("Done")
