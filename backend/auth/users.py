from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from auth.auth import auth_backend
from auth.manager import get_user_manager
from models.user import User
from schemas.user import UserBase, UserCreate, UserUpdate

fastapi_users = FastAPIUsers[User, str](
    get_user_manager,
    [auth_backend]
)

router = APIRouter()

router.include_router(
    fastapi_users.get_users_router(UserBase, UserUpdate),
    prefix="/users",
    tags=["users"]
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"]
)
