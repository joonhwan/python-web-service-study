from enum import Enum, IntEnum
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from .user import User


class GemType(str, Enum):
    DIAMOND = "DIAMOND"
    RUBY = "RUBY"
    EMERALD = "EMERALD"


class GemClarity(IntEnum):
    SI = 1
    VS = 2
    VVS = 3
    FL = 4


class GemColor(str, Enum):
    D = 'D'
    E = 'E'
    G = 'G'
    F = 'F'
    H = 'H'
    I = 'I'


class GemProperties(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    size: float = 1.0
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None
    # relationship attributes(EF Core의 Navigation Properties)
    #    'Gem' 은 뒤에 선언된 타입을 사용하기 위함?
    gem: Optional['Gem'] = Relationship(back_populates="gem_properties")


class Gem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    price: float = 0.0
    gem_type: Optional[GemType] = GemType.DIAMOND
    gem_properties_id: Optional[int] = Field(default=None, foreign_key=GemProperties.id)
    seller_id: Optional[int] = Field(default=None, foreign_key=User.id)
    # relationship attributes(EF Core의 Navigation Properties)
    gem_properties: Optional[GemProperties] = Relationship(back_populates='gem')
    seller: Optional[User] = Relationship()
