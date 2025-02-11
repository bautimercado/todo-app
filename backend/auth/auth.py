import os

from fastapi_users.authentication import JWTStrategy
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

auth_backend = JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)
