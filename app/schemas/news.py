from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsBase(BaseModel):
    title: str
    slug: str
    image_url: Optional[str] = None
    short_description: Optional[str] = None
    content: str
    category: Optional[str] = "Tech"

class NewsCreate(NewsBase):
    pass

class NewsUpdate(NewsBase):
    title: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None

class News(NewsBase):
    id: int
    published_at: datetime
    likes: int = 0
    author_id: Optional[int] = None
    author_name: Optional[str] = None
    author_avatar: Optional[str] = None

    class Config:
        from_attributes = True
