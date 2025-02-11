from typing import List

from pydantic import BaseModel

from backend.schemas.task import TaskResponse

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: str
    is_active: bool
    tasks: List[TaskResponse] = []

    class Config:
        from_attributes = True
