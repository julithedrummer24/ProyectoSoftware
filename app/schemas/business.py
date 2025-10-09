from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Business Schemas
class BusinessBase(BaseModel):
    name: str
    address: str
    opening_time: Optional[datetime] = None
    closing_time: Optional[datetime] = None

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    business_id: int
    
    class Config:
        from_attributes = True