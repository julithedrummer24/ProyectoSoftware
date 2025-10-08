from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    reservation_id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey('services.service_id'))
    date_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    status = Column(String, default='pending')  # pending, confirmed, cancelled, attended

    # Relationships
    service = relationship("Service", back_populates="reservations")
    relationships = relationship("ClientStaffReservation", back_populates="reservation")

    def __repr__(self):
        return f"<Reservation(id={self.reservation_id}, status={self.status})>"
