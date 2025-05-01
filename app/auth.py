import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException

fake_user = {
    "username": "admin",
    "password": "admin123"
}

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_dev_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_credentials(username: str, password: str):
    return username == fake_user["username"] and password == fake_user["password"]

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
