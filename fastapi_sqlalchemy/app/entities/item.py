from typing import TYPE_CHECKING
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.env import Base

if TYPE_CHECKING:
    from .user import UserEntity  # noqa: F401

class ItemEntity(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserEntity", back_populates="items")