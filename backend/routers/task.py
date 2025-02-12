from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from auth.users import fastapi_users
from schemas.task import TaskResponse, TaskCreate, TaskUpdate
from services.task import get_tasks, get_task, create_task, update_task, delete_task
from models.user import User

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
async def list_tasks(db: AsyncSession = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    return await get_tasks(db, user.id)


@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    task = await get_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@router.post("/", response_model=TaskResponse)
async def create_new_task(task_data: TaskCreate, db: AsyncSession = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    return await create_task(db, task_data, user.id)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_existing_task(task_id: int, task_data: TaskUpdate, db: AsyncSession = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    task = await update_task(db, task_id, task_data, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@router.delete("/{task_id}")
async def delete_existing_task(task_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(fastapi_users.current_user())):
    task = await delete_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada"}
