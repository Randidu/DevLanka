from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    instructor = Column(String)
    duration = Column(String) # e.g. "10 hours"
    level = Column(String) # Beginner, Intermediate, Advanced
    thumbnail = Column(String, nullable=True)
    url = Column(String)
    price = Column(Float, default=0.0)
    is_free = Column(Boolean, default=True)
