import logging
from typing import Callable
from sqlmodel import SQLModel, create_engine, Session
from hero.util.logging import configure_log_handler

DB_URL = "postgresql://postgres:postgres@localhost:15432"
engine = create_engine(f"{DB_URL}/hero")


def init_db(*, log_level=logging.WARNING):
    configure_log_handler(log_level=log_level)
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

