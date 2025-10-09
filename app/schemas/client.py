from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Client Schemas
class ClientBase(BaseModel):
    user_id: int

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    client_id: int
    registration_date: datetime
    
    class Config:
        from_attributes = True
