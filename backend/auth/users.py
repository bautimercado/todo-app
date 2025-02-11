from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from backend.models.user import User

fastapi_users = FastAPIUsers[User, str](
    get_user_manager,
    [auth_backend],
)

user_router = fastapi_users.get_users_router()
auth_router = fastapi_users.get_auth_router(auth_backend)

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
