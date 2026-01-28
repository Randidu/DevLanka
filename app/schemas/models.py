from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.database import Base

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
    
    # Relationships
    tickets = relationship("SupportTicket", back_populates="user")

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    image_url = Column(String)
    short_description = Column(String)
    content = Column(Text)
    category = Column(String, index=True) # AI, Web, Mobile, etc.
    published_at = Column(DateTime(timezone=True), server_default=func.now())
    author_id = Column(Integer, ForeignKey("users.id"))

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    platform = Column(String) # Coursera, Udemy
    is_free = Column(Boolean, default=True)
    language = Column(String)
    level = Column(String) # Beginner, Intermediate
    category = Column(String)
    link = Column(String)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    embed_url = Column(String)
    channel_name = Column(String)
    language = Column(String) # Sinhala, English, Tamil
    category = Column(String)
    level = Column(String)

class TicketStatus(str, enum.Enum):
    PENDING = "pending"
    REPLIED = "replied"
    CLOSED = "closed"

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    message = Column(Text)
    category = Column(String) # Bug, Content Request, etc.
    status = Column(String, default=TicketStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="tickets")
