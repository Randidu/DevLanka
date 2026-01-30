from pydantic import BaseModel
from typing import List, Optional

class ResourceBase(BaseModel):
    title: str
    description: Optional[str] = None
    url: str
    icon: Optional[str] = None
    category_id: Optional[int] = None
    is_approved: bool = False

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(ResourceBase):
    title: Optional[str] = None
    url: Optional[str] = None
    category_id: Optional[int] = None
    is_approved: Optional[bool] = None

class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True

class ResourceCategoryBase(BaseModel):
    name: str
    slug: str
    icon: Optional[str] = None

class ResourceCategoryCreate(ResourceCategoryBase):
    pass

class ResourceCategoryUpdate(ResourceCategoryBase):
    name: Optional[str] = None
    slug: Optional[str] = None

class ResourceCategory(ResourceCategoryBase):
    id: int
    resources: List[Resource] = []

    class Config:
        from_attributes = True
