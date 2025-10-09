from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# BusinessStaff Schemas
class BusinessStaffBase(BaseModel):
    user_id: int
    business_id: int
    position: str

class BusinessStaffCreate(BusinessStaffBase):
    pass

class BusinessStaff(BusinessStaffBase):
    staff_id: int
    
    class Config:
        from_attributes = True