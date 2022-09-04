import asyncio
from unittest import async_case
from loguru import logger
from sqlmodel import select, text
from hero.models import Hero
from hero.db_async import init_db, get_session, async_session, engine

async def delete_heroes():
    async with async_session() as session:
        async with session.begin():
            await session.execute(text("DELETE FROM hero"))

async def create_heroes():
    heroes = [
        Hero(name="superman", secret_name="Clark Kent"),
        Hero(name="batman", secret_name="Bruce Wayne"),
        Hero(name="ironman", secret_name="Tony Stark"),
        # Hero(name="spiderman", secret_name="Peter Parker"),
        # Hero(name="hulk", secret_name="Bruce Banner"),
        # Hero(name="wolverine", secret_name="James Howlett"),
        # Hero(name="thor", secret_name="Thor Odinson"),
        # Hero(name="captain america", secret_name="Steve Rogers"),
    ]
    logger.info("-- commit() 전 hero")
    for idx, hero in enumerate(heroes):
        logger.info(" hero[{idx}] {hero}", idx=idx, hero=hero)
        

    async with async_session() as session:
        async with session.begin():
            for hero in heroes:
                session.add(hero)

        await session.commit()

        logger.info("-- commit() 후 hero")
        for idx, hero in enumerate(heroes):
            # logger.info(" hero[{idx}] {hero}", idx=idx, hero=hero)
            logger.info(" hero[{idx}] id='{id}', name='{name}'", idx=idx, id=hero.id, name=hero.name)
            next_id = hero.id + 1
            logger.debug('next_id = {next_id}', next_id=next_id)

        for idx, hero in enumerate(heroes):
            await session.refresh(hero)
            logger.warning(" hero[{idx}] {hero}", idx=idx, hero=hero or {})
    
    logger.info("-- with 밖 hero")
    for idx, hero in enumerate(heroes):
        logger.info(" hero[{idx}] {hero}", idx=idx, hero=hero)



async def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    import logging
    await init_db(log_level=logging.INFO)
    await delete_heroes()
    await create_heroes()


if __name__ == "__main__":
    logger.info("begin")
    asyncio.run(main())
    print("Done")
