from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from auth.users import fastapi_users
from schemas.task import TaskResponse, TaskCreate, TaskUpdate
from services.task import get_tasks, get_task, create_task, update_task, delete_task
from models.user import User

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
async def list_tasks(db: Session = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    return get_tasks(db, user.id)


@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int, db: Session = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    task = get_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@router.post("/", response_model=TaskResponse)
async def create_new_task(task_data: TaskCreate, db: Session = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    return create_task(db, task_data, user.id)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_existing_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    task = update_task(db, task_id, task_data, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@router.delete("/{task_id}")
async def delete_existing_task(task_id: int, db: Session = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    task = delete_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada"}
