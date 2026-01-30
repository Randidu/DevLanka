from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Pathway(Base):
    __tablename__ = "pathways"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True) # e.g., 'web', 'mobile'
    title = Column(String)
    description = Column(String)
    icon = Column(String, nullable=True)
    
    steps = relationship("PathwayStep", back_populates="pathway", cascade="all, delete-orphan")

class PathwayStep(Base):
    __tablename__ = "pathway_steps"

    id = Column(Integer, primary_key=True, index=True)
    pathway_id = Column(Integer, ForeignKey("pathways.id"))
    step_number = Column(Integer)
    title = Column(String)
    description = Column(String)
    step_type = Column(String) # 'left' or 'right'
    video_id = Column(String, nullable=True)
    resource_url = Column(String, nullable=True)
    
    pathway = relationship("Pathway", back_populates="steps")
