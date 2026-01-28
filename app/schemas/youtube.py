from pydantic import BaseModel
from typing import Optional

class TutorialBase(BaseModel):
    title: str
    description: Optional[str] = None
    video_id: str
    channel_title: Optional[str] = None
    view_count: Optional[int] = 0
    category: Optional[str] = "Tech"
    thumbnail_url: Optional[str] = None

class TutorialCreate(TutorialBase):
    pass

class TutorialUpdate(TutorialBase):
    title: Optional[str] = None
    video_id: Optional[str] = None

class Tutorial(TutorialBase):
    id: int
    duration: Optional[int] = 0

    class Config:
        from_attributes = True
