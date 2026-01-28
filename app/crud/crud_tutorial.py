from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.youtube import Tutorial
from app.schemas.youtube import TutorialCreate, TutorialUpdate

class CRUDTutorial(CRUDBase[Tutorial, TutorialCreate, TutorialUpdate]):
    def get_multi_by_category(
        self, db: Session, *, category: str, skip: int = 0, limit: int = 100
    ) -> List[Tutorial]:
        return (
            db.query(self.model)
            .filter(Tutorial.category == category)
            .offset(skip)
            .limit(limit)
            .all()
        )

tutorial = CRUDTutorial(Tutorial)
