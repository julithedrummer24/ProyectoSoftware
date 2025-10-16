from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# User Schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    
    class Config:
        from_attributes = True