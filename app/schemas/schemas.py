from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    hashed_password: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str