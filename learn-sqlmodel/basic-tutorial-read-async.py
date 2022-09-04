import asyncio
from typing import List
from loguru import logger
from sqlmodel import select, or_, text
from hero.models import Hero
from hero.db_async import init_db, get_session, async_session, engine

async def delete_heroes():
    async with async_session() as session:
        async with session.begin():
            await session.execute(text("DELETE FROM hero"))

async def create_heroes():
    heroes = [
        Hero(name="superman", secret_name="Clark Kent", age=30),
        Hero(name="batman", secret_name="Bruce Wayne", age=40),
        Hero(name="ironman", secret_name="Tony Stark", age=50),
        Hero(name="spiderman", secret_name="Peter Parker", age=19),
        Hero(name="hulk", secret_name="Bruce Banner", age=32),
        Hero(name="wolverine", secret_name="James Howlett",age=35),
        Hero(name="thor", secret_name="Thor Odinson", age=25),
        Hero(name="captain america", secret_name="Steve Rogers"),
    ]

    async with async_session() as session:
        for hero in heroes:
            session.add(hero)
        await session.commit()


async def read_heroes():
    async with async_session() as session:
        # result = await session.exec(select(Hero).where(Hero.name == "superman"))
        # result = await session.exec(select(Hero).where(Hero.age > 30).where(Hero.age < 50))
        result = await session.exec(select(Hero).where(or_(Hero.age < 20, Hero.age >= 40)))
        
        # heroes = result.all()
        # for hero in heroes:
        #     logger.info("{hero} {type}", hero=hero, type=type(hero))
        
        first_hero:Hero = result.first()
        logger.error('First Hero : {hero}', hero=first_hero)

async def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    import logging
    await init_db(log_level=logging.INFO)
    # await delete_heroes()
    # await create_heroes()
    await read_heroes()


if __name__ == "__main__":
    logger.info("begin")
    asyncio.run(main())
    print("Done")
