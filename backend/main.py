from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.auth.users import router as auth_router, user_router
from backend.routers.task import router as task_router
from backend.config.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description="API para una aplicación de gestión de tareas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router, prefix="/tasks", tags=["tasks"])

@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}
