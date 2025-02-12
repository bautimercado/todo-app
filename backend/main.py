from contextlib import asynccontextmanager

from auth.users import router as auth_router
from config.database import create_db_and_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.task import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(
    title="Todo API",
    description="API para una aplicación de gestión de tareas",
    version="1.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(task_router, prefix="/tasks", tags=["tasks"])

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}
