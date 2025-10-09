from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Reservation Schemas
class ReservationBase(BaseModel):
    service_id: int
    date_time: datetime
    status: str = "pending"

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    reservation_id: int
    
    class Config:
        from_attributes = True