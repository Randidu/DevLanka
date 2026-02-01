from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.news import News
from app.schemas.news import NewsCreate, NewsUpdate

from sqlalchemy.orm import joinedload

class CRUDNews(CRUDBase[News, NewsCreate, NewsUpdate]):
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[News]:
        return db.query(self.model).options(joinedload(News.author)).offset(skip).limit(limit).all()

    def get_multi_by_category(
        self, db: Session, *, category: str, skip: int = 0, limit: int = 100
    ) -> List[News]:
        return (
            db.query(self.model)
            .options(joinedload(News.author))
            .filter(News.category == category)
            .offset(skip)
            .limit(limit)
            .all()
        )

news = CRUDNews(News)
