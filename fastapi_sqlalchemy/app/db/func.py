from loguru import logger
from .env import Base, engine, Session

def init_db():
    logger.info("😃 Initializing database...")
    Base.metadata.create_all(bind=engine)

# dependencies
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
