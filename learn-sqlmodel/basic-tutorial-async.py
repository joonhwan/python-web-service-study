import asyncio
from loguru import logger
from hero.models import Hero
from hero.db_async import init_db

async def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    await init_db()

if __name__ == "__main__":
    logger.info("begin")
    asyncio.run(main())
    print("Done")
