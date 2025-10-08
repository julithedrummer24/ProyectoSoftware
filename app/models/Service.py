from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Service(Base):
    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('businesses.business_id'))
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # minutes
    price = Column(Float, nullable=False)

    # Relationships
    business = relationship("Business", back_populates="services")
    reservations = relationship("Reservation", back_populates="service")

    def __repr__(self):
        return f"<Service(name={self.name}, business_id={self.business_id})>"