
from typing import Optional
from pydantic import BaseModel

from jewel_app.models.gem import GemType

class GemCreate(BaseModel):
    price: float = 0.0
    gem_type: Optional[str] = None
    gem_properties_id: Optional[int] = None
    seller_id: Optional[int] = None

class GemPatch(BaseModel):
    id: int 
    price: Optional[float] = None
    available: Optional[bool] = None
    gem_type: Optional[GemType] = None
    gem_properties_id: Optional[int] = None

