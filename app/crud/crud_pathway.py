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
            icon=obj_in.icon
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

    def update(self, db: Session, *, db_obj: Pathway, obj_in: PathwayUpdate) -> Pathway:
        obj_data = obj_in.dict(exclude_unset=True)
        
        # Handle 'steps' separately
        steps_data = obj_data.pop("steps", None)
        
        # Update basic fields
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
            
        if steps_data is not None:
            # Clear existing steps (cascade should handle deletion)
            db_obj.steps = []
            
            # Add new steps
            for step_in in steps_data:
                # step_in is a dict here because obj_in.dict() converts sub-models to dicts
                db_step = PathwayStep(
                    pathway_id=db_obj.id,
                    **step_in
                )
                db.add(db_step)
                # Note: appending to db_obj.steps also works but explicit add is safe
                # db_obj.steps.append(db_step) 

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

pathway = CRUDPathway(Pathway)
