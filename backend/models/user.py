from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")
