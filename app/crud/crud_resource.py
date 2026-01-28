from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.resource import Resource, ResourceCategory
from app.schemas.resource import ResourceCreate, ResourceUpdate, ResourceCategoryCreate, ResourceCategoryUpdate

class CRUDResource(CRUDBase[Resource, ResourceCreate, ResourceUpdate]):
    def get_multi_by_category(
        self, db: Session, *, category_id: int, skip: int = 0, limit: int = 100
    ) -> List[Resource]:
        return (
            db.query(self.model)
            .filter(Resource.category_id == category_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

class CRUDResourceCategory(CRUDBase[ResourceCategory, ResourceCategoryCreate, ResourceCategoryUpdate]):
    def get_by_slug(self, db: Session, *, slug: str) -> ResourceCategory:
        return db.query(self.model).filter(ResourceCategory.slug == slug).first()

resource = CRUDResource(Resource)
resource_category = CRUDResourceCategory(ResourceCategory)
