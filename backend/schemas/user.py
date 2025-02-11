from typing import Optional, List

from pydantic import BaseModel

from backend.schemas.task import TaskResponse

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    is_active: bool
    tasks: List[TaskResponse] = []

    class Config:
        orm_mode = True
