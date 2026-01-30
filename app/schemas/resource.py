from pydantic import BaseModel
from typing import List, Optional

class ResourceBase(BaseModel):
    title: str
    description: Optional[str] = None
    url: str
    icon: Optional[str] = None
    category_id: Optional[int] = None
    is_approved: bool = False
    type: Optional[str] = None
    language: Optional[str] = "English"
    images: Optional[str] = None

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(ResourceBase):
    title: Optional[str] = None
    url: Optional[str] = None
    category_id: Optional[int] = None
    is_approved: Optional[bool] = None

class ResourceOwner(BaseModel):
    id: int
    full_name: Optional[str] = None
    avatar: Optional[str] = None
    
    class Config:
        from_attributes = True

class Resource(ResourceBase):
    id: int
    owner_id: Optional[int] = None
    images: Optional[str] = None
    owner: Optional[ResourceOwner] = None

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
