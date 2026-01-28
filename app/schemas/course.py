from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    instructor: Optional[str] = None
    duration: Optional[str] = None
    level: Optional[str] = "Beginner"
    thumbnail: Optional[str] = None
    url: str
    price: float = 0.0
    is_free: bool = True

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    title: Optional[str] = None
    url: Optional[str] = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True
