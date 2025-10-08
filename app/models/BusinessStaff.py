from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class BusinessStaff(Base):
    __tablename__ = 'business_staff'

    staff_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    business_id = Column(Integer, ForeignKey('businesses.business_id'))
    position = Column(String, nullable=False)

    # Relationships
    user = relationship("User", back_populates="staff")
    business = relationship("Business", back_populates="staff")
    staff_reservations = relationship("ClientStaffReservation", back_populates="staff")

    def __repr__(self):
        return f"<BusinessStaff(user_id={self.user_id}, position={self.position})>"