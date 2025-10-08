from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    registration_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    user = relationship("User", back_populates="client")
    addresses = relationship("Address", back_populates="client")
    client_reservations = relationship("ClientStaffReservation", back_populates="client")

    def __repr__(self):
        return f"<Client(id={self.client_id}, user={self.user_id})>"