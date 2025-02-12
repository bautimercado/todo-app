from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    tasks = relationship("Task", back_populates="owner")
