from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    director: str | None = None


# creation model
class MovieCreate(MovieBase):
    pass

# read model
class Movie(MovieBase):
    id: int
    class Config:
        orm_mode = True
