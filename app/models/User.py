from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # client, admin, staff

    # Relationships
    client = relationship("Client", back_populates="user", uselist=False)
    staff = relationship("BusinessStaff", back_populates="user", uselist=False)

    def __repr__(self):
        return f"<User(name={self.name}, role={self.role})>"