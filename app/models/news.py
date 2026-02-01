from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

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
    likes = Column(Integer, default=0)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("app.models.user.User", back_populates="news_posts")
    comments = relationship("app.models.comment.Comment", back_populates="news", cascade="all, delete-orphan")
