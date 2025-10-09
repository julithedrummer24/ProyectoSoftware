from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Address Schemas
class AddressBase(BaseModel):
    client_id: int
    full_address: str

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    address_id: int
    
    class Config:
        from_attributes = True