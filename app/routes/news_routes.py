from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas.news import News, NewsCreate, NewsUpdate
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[News])
def read_news_multi(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category: str = None
) -> Any:
    """
    Retrieve news.
    """
    if category:
        return crud.news.get_multi_by_category(db, category=category, skip=skip, limit=limit)
    news = crud.news.get_multi(db, skip=skip, limit=limit)
    return news

from app.core.deps import get_current_user
from app.models.user import User as UserModel

from typing import Optional

@router.post("/", response_model=News)
def create_news(
    *,
    db: Session = Depends(get_db),
    news_in: NewsCreate,
    current_user: Optional[UserModel] = Depends(lambda: None)  # Make auth optional
) -> Any:
    """
    Create new news post.
    """
    news_data = news_in.dict()
    # Set author_id to 1 (admin) if no user is authenticated
    news_data['author_id'] = current_user.id if current_user else 1
    news = crud.news.create(db, obj_in=news_data)
    return news

@router.get("/{news_id}", response_model=News)
def read_news(
    *,
    db: Session = Depends(get_db),
    news_id: int
) -> Any:
    """
    Get news by ID.
    """
    news = crud.news.get(db, id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news

@router.put("/{news_id}", response_model=News)
def update_news(
    *,
    db: Session = Depends(get_db),
    news_id: int,
    news_in: NewsUpdate
) -> Any:
    """
    Update a news post.
    """
    news = crud.news.get(db, id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    news = crud.news.update(db, db_obj=news, obj_in=news_in)
    return news

@router.delete("/{news_id}", response_model=News)
def delete_news(
    *,
    db: Session = Depends(get_db),
    news_id: int
) -> Any:
    """
    Delete a news post.
    """
    news = crud.news.get(db, id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    news = crud.news.remove(db, id=news_id)
    return news
