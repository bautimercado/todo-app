from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base

class Task(Base):
    __annotations__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")
