from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud
from app.schemas.user import User, UserCreate, UserUpdate
from app.core.database import get_db

router = APIRouter()

from datetime import timedelta
from app.core import security
from app.config import settings
from pydantic import BaseModel
import random
import string
from app.utils.email import send_verification_email

def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

class VerifyRequest(BaseModel):
    email: str
    code: str

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
            detail="The user with this email already exists in the system.",
        )
    print(f"Registering user: {user_in.email}")
    user = crud.user.create(db, obj_in=user_in)
    
    # Generate verification code
    code = generate_verification_code()
    user.verification_code = code
    user.is_verified = False
    db.add(user)
    db.commit()
    db.refresh(user)
    
    # Send email
    print(f"Sending email to {user.email}")
    email_status = send_verification_email(user.email, code)
    print(f"Email sent status: {email_status}")
    
    return user

@router.post("/verify")
def verify_email(
    verify_in: VerifyRequest,
    db: Session = Depends(get_db)
):
    user = crud.user.get_by_email(db, email=verify_in.email)
    if not user:
         raise HTTPException(status_code=404, detail="User not found")
    
    if user.is_verified:
        return {"message": "Email already verified"}

    if user.verification_code == verify_in.code:
        user.is_verified = True
        user.verification_code = None 
        db.add(user)
        db.commit()
        return {"message": "Email verified successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid verification code")

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
        "role": user.role,
        "full_name": user.full_name
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
    *,
    db: Session = Depends(get_db),
    user_in: UserUpdate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Update own user.
    """
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user

@router.delete("/users/{user_id}", response_model=User)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
) -> Any:
    """
    Delete a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.remove(db, id=user_id)
    return user

@router.put("/users/{user_id}", response_model=User)
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db)
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user

import uuid
from datetime import datetime
from app.utils.email import send_password_reset_email
from app.core.security import get_password_hash

class ForgotPasswordRequest(BaseModel):
    email: str

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str

@router.post("/forgot-password")
def forgot_password(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    user = crud.user.get_by_email(db, email=request.email)
    if not user:
        # Return 200 even if user not found to prevent email enumeration
        return {"message": "If this email exists, a password reset link has been sent."}

    # Generate Token
    token = str(uuid.uuid4())
    user.reset_token = token
    user.reset_token_expires = datetime.utcnow() + timedelta(minutes=30)
    db.add(user)
    db.commit()

    # Construct Link
    base_url = "http://127.0.0.1:8000"
    if settings.POSTGRES_SERVER != "localhost":
         base_url = "https://youtube-video-downloader-x1hn.onrender.com"
    
    reset_link = f"{base_url}/reset-password.html?token={token}"
    
    send_password_reset_email(user.email, reset_link)
    
    return {"message": "Password reset link sent"}

@router.post("/reset-password")
def reset_password(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    user = db.query(crud.user.model).filter(crud.user.model.reset_token == request.token).first()
    
    if not user:
         raise HTTPException(status_code=400, detail="Invalid or expired token")
    
    if user.reset_token_expires < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Token expired")
        
    # Update Password
    user.hashed_password = get_password_hash(request.new_password)
    user.reset_token = None
    user.reset_token_expires = None
    db.add(user)
    db.commit()
    
    return {"message": "Password updated successfully"}
