from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from backend.config.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __annotations__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")
