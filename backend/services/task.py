import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.task import Task
from schemas.task import TaskCreate, TaskUpdate


async def get_tasks(db: AsyncSession, user_id: uuid.UUID):
    result = await db.execute(
        select(Task).filter(Task.owner_id == user_id)
    )
    return result.scalars().all()

async def get_task(db: AsyncSession, task_id: int, user_id: uuid.UUID):
    result = await db.execute(
        select(Task).filter(Task.owner_id == user_id, Task.id == task_id)
    )
    return result.scalars().first()

async def create_task(db: AsyncSession, task_data: TaskCreate, user_id: uuid.UUID):
    new_task = Task(**task_data.model_dump(), owner_id=user_id)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


async def update_task(db: AsyncSession, task_id: int, task_data: TaskUpdate, user_id: uuid.UUID):
    result = await db.execute(select(Task).filter(Task.id == task_id, Task.owner_id == user_id))
    task = result.scalars().first()
    if not task:
        return None
    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: int, user_id: uuid.UUID):
    result = await db.execute(select(Task).filter(Task.id == task_id, Task.owner_id == user_id))
    task = result.scalars().first()
    if not task:
        return None
    await db.delete(task)
    await db.commit()
    return task
