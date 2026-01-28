from typing import List, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.pathway import Pathway, PathwayStep
from app.schemas.pathway import PathwayCreate, PathwayUpdate, PathwayStepCreate

class CRUDPathway(CRUDBase[Pathway, PathwayCreate, PathwayUpdate]):
    def get_by_slug(self, db: Session, *, slug: str) -> Optional[Pathway]:
        return db.query(self.model).filter(Pathway.slug == slug).first()

    def create(self, db: Session, *, obj_in: PathwayCreate) -> Pathway:
        db_obj = Pathway(
            slug=obj_in.slug,
            title=obj_in.title,
            description=obj_in.description,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        for step_in in obj_in.steps:
            db_step = PathwayStep(
                pathway_id=db_obj.id,
                **step_in.dict()
            )
            db.add(db_step)
        
        db.commit()
        db.refresh(db_obj)
        return db_obj

pathway = CRUDPathway(Pathway)
