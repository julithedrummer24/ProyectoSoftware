from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Service Schemas
class ServiceBase(BaseModel):
    business_id: int
    name: str
    duration: int
    price: float

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    service_id: int
    
    class Config:
        from_attributes = True