import asyncio
import logging
from loguru import logger
from hero.models import Hero
from hero.db import init_db

def main():
    # Model(여기서는 hero) 가 import 된 다음 init_db() 호출(SQLModel.metadata.create_all())
    init_db(log_level=logging.DEBUG)

if __name__ == "__main__":
    logger.info("begin")
    main()
    logger.info("done")
