from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud
from app.schemas.user import User, UserCreate, UserUpdate
from app.core.database import get_db

router = APIRouter()

@router.post("/register", response_model=User)
def register_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user

from datetime import timedelta
from app.core import security
from app.config import settings
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(
    item: LoginRequest,
    db: Session = Depends(get_db)
) -> Any:
    """
    Login user.
    """
    user = crud.user.authenticate(db, email=item.email, password=item.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=user.id, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "email": user.email,
        "role": user.role
    }

from app.core.deps import get_current_user

@router.get("/me", response_model=User)
def read_user_me(
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Get current user.
    """
    return current_user

@router.get("/users", response_model=List[User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.put("/me", response_model=User)
def update_user_me(
    user_id: int, # Mocking current user for now
    *,
    db: Session = Depends(get_db),
    user_in: UserUpdate
) -> Any:
    """
    Update own user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
