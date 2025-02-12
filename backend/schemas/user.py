import uuid

from typing import List
from pydantic import EmailStr
from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from schemas.task import TaskResponse

class UserBase(BaseUser[uuid.UUID]):
    username: EmailStr

class UserCreate(BaseUserCreate):
    username: EmailStr
    password: str

class UserUpdate(BaseUserUpdate):
    username: EmailStr
    password: str

class UserResponse(UserBase):
    tasks: List[TaskResponse] = []

    class Config:
        from_attributes = True
