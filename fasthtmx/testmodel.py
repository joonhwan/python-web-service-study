from loguru import logger
# 순서가 중요하다 😳
from fasthtmx.schema import Hero
from fasthtmx.db import init_db, new_session
from sqlmodel import select

def add_heroes():
    heroes = [
        # Hero(id=1, name="superman", secret_name="Clark Kent", age=30),
        # Hero(id=2, name="batman", secret_name="Bruce Wayne", age=40),
        # Hero(id=3, name="flash", secret_name="Barry Allen", age=20),
        Hero(name="wolverine", secret_name="James Howlett", age=30),
        Hero(name="spiderman", secret_name="Peter Parker", age=20),
        Hero(name="supergirl", secret_name="Kara Zor-El", age=30),
        Hero(name="cyborg", secret_name="sentinel", age=20),
        Hero(name="catwoman", secret_name="Kitty Pryde", age=40),
        Hero(name="aquaman", secret_name="Arthur Curry", age=30),
        Hero(name="green arrow", secret_name="Oliver Queen", age=20),
    ]

    with new_session() as session:
        session.add_all(heroes)
        session.commit()

def select_heroes():
    with new_session() as session:
        query = select(Hero).where(Hero.name == "aquaman")
        hero = session.execute(query).first()
        logger.info(f"hero : {hero}")
        # logger.info(f"found : {hero} is {hero.age} years old")
        

if __name__ == "__main__":
    init_db()
    add_heroes()
    select_heroes()
    logger.info("done")