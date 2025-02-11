from sqlalchemy.orm import Session
from backend.models.task import Task
from backend.schemas.task import TaskCreate, TaskUpdate


def get_tasks(db: Session, user_id: str):
    return db.query(Task).filter(Task.owner_id == user_id).all()


def get_task(db: Session, task_id: int, user_id: str):
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()


def create_task(db: Session, task_data: TaskCreate, user_id: str):
    new_task = Task(**task_data.model_dump(), owner_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: str):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
    if not task:
        return None
    for key, value in task_data.model_dump().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int, user_id: str):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
