from pydantic import BaseModel
from typing import List, Optional

class PathwayStepBase(BaseModel):
    step_number: int
    title: str
    description: Optional[str] = None
    step_type: Optional[str] = "left"
    video_id: Optional[str] = None

class PathwayStepCreate(PathwayStepBase):
    pass

class PathwayStepUpdate(PathwayStepBase):
    step_number: Optional[int] = None
    title: Optional[str] = None

class PathwayStep(PathwayStepBase):
    id: int
    pathway_id: int

    class Config:
        from_attributes = True

class PathwayBase(BaseModel):
    slug: str
    title: str
    description: Optional[str] = None

class PathwayCreate(PathwayBase):
    steps: List[PathwayStepCreate]

class PathwayUpdate(PathwayBase):
    slug: Optional[str] = None
    title: Optional[str] = None
    steps: Optional[List[PathwayStepCreate]] = None

class Pathway(PathwayBase):
    id: int
    steps: List[PathwayStep] = []

    class Config:
        from_attributes = True
