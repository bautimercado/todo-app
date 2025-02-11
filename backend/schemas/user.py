from typing import List

from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate

from backend.schemas.task import TaskResponse

class UserBase(BaseUser):
    pass

class UserCreate(BaseUserCreate):
    pass

class UserUpdate(BaseUserUpdate):
    pass

class UserResponse(UserBase):
    id: str
    is_active: bool
    tasks: List[TaskResponse] = []

    class Config:
        from_attributes = True
