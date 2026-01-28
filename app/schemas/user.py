from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: Optional[str] = "student"
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class User(UserBase):
    id: int
    avatar: Optional[str] = None

    class Config:
        from_attributes = True
