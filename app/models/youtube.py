from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    video_id = Column(String, unique=True, index=True) # YouTube video ID
    duration = Column(Integer) # In seconds
    thumbnail_url = Column(String, nullable=True)
    channel_title = Column(String, nullable=True)
    view_count = Column(Integer, default=0)
    category = Column(String, nullable=True) # e.g. "Python", "Web", "Mobile"
