from fastapi_users import BaseUserManager, UUIDIDMixin
from backend.config.database import get_user_db
from backend.models.user import User
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

class UserManager(UUIDIDMixin, BaseUserManager[User, str]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

async def get_user_manager(user_db=next(get_user_db())):
    yield UserManager(user_db)
