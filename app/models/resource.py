from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class ResourceCategory(Base):
    __tablename__ = "resource_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    slug = Column(String, unique=True, index=True)
    icon = Column(String, nullable=True)
    
    resources = relationship("Resource", back_populates="category")

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    url = Column(String)
    icon = Column(String, nullable=True) # Emoji or image URL
    is_approved = Column(Boolean, default=False)

    
    category_id = Column(Integer, ForeignKey("resource_categories.id"))
    category = relationship("ResourceCategory", back_populates="resources")
