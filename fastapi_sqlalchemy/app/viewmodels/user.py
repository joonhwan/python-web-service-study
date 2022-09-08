from typing import List, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .item import Item

class UserBase(BaseModel):
    email: str

# creation model
class UserCreate(UserBase):
    password: str

# read model
class User(UserBase):
    id: int
    is_active: bool
    items: List["Item"] = []

    class Config:
        orm_mode = True