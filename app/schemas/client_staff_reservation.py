from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ClientStaffReservation Schemas
class ClientStaffReservationBase(BaseModel):
    reservation_id: int
    client_id: int
    staff_id: int

class ClientStaffReservationCreate(ClientStaffReservationBase):
    pass

class ClientStaffReservation(ClientStaffReservationBase):
    csr_id: int
    
    class Config:
        from_attributes = True