from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

# creation model
class ItemCreate(ItemBase):
    pass

# read model
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

