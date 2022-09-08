from typing import TYPE_CHECKING
from sqlalchemy import Column, Index, Integer, String, Identity, Sequence, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.env import Base

if TYPE_CHECKING:
    from .item import ItemEntity


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("ItemEntity", back_populates="owner")


