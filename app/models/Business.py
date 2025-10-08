from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Business(Base):
    __tablename__ = 'businesses'

    business_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    opening_time = Column(DateTime, nullable=True)
    closing_time = Column(DateTime, nullable=True)

    # Relationships
    staff = relationship("BusinessStaff", back_populates="business")
    services = relationship("Service", back_populates="business")

    def __repr__(self):
        return f"<Business(name={self.name})>"