from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Address(Base):
    __tablename__ = 'addresses'

    address_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.client_id'))
    full_address = Column(String, nullable=False)

    # Relationships
    client = relationship("Client", back_populates="addresses")

    def __repr__(self):
        return f"<Address(client_id={self.client_id})>"