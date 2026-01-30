from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    STUDENT = "student"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default=UserRole.STUDENT)
    avatar = Column(String, nullable=True)
    verification_code = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    
    # Relationships
    tickets = relationship("app.models.support.SupportTicket", back_populates="user")
    news_posts = relationship("app.models.news.News", back_populates="author")
