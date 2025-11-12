from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# User Schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "client"

class User(UserBase):
    user_id: int
    
    class Config:
        from_attributes = True
        
class UserUpdate(UserBase):
    password: Optional[str] = None
    role: Optional[str] = None