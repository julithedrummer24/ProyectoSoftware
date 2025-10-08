from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class ClientStaffReservation(Base):
    __tablename__ = 'client_staff_reservations'

    csr_id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey('reservations.reservation_id'))
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    staff_id = Column(Integer, ForeignKey('business_staff.staff_id'))

    # Relationships
    reservation = relationship("Reservation", back_populates="relationships")
    client = relationship("Client", back_populates="client_reservations")
    staff = relationship("BusinessStaff", back_populates="staff_reservations")

    def __repr__(self):
        return f"<CSR(reservation_id={self.reservation_id}, client_id={self.client_id})>"