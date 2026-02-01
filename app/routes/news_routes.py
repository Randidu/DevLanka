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
        news_list = crud.news.get_multi_by_category(db, category=category, skip=skip, limit=limit)
    else:
        news_list = crud.news.get_multi(db, skip=skip, limit=limit)
        
    for item in news_list:
        if item.author:
            item.author_name = item.author.full_name
            item.author_avatar = item.author.avatar
            
    return news_list

from app.core.deps import get_current_user
from app.models.user import User as UserModel

from typing import Optional

@router.post("/", response_model=News)
def create_news(
    *,
    db: Session = Depends(get_db),
    news_in: NewsCreate,
    current_user: UserModel = Depends(get_current_user)
) -> Any:
    """
    Create new news post.
    """
    with open("debug_news.log", "a") as f:
        f.write(f"INCOMING: {news_in.dict()}\n")
    
    news_data = news_in.dict()
    news_data['author_id'] = current_user.id
    with open("debug_news.log", "a") as f:
        f.write(f"FINAL TO DB: {news_data}\n")
    news = crud.news.create(db, obj_in=news_data)
    
    # Manually populate author info
    news.author_name = current_user.full_name
    news.author_avatar = current_user.avatar
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
    news = crud.news.remove(db, id=news_id)
    return news

from app.schemas.comment import Comment, CommentCreate
from app.models.comment import Comment as CommentModel
from app.core.deps import get_current_user

@router.post("/{news_id}/comments", response_model=Comment)
def create_comment(
    *,
    db: Session = Depends(get_db),
    news_id: int,
    comment_in: CommentCreate,
    current_user: UserModel = Depends(get_current_user)
) -> Any:
    """
    Create a new comment for a news post.
    """
    # Check if news exists
    news = crud.news.get(db, id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News post not found")
        
    db_obj = CommentModel(
        content=comment_in.content,
        author_id=current_user.id,
        news_id=news_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    # Manually populate author_name for response if needed, 
    # but Pydantic might need the relation loaded or a custom schema.
    # Our schema expects author_name.
    db_obj.author_name = current_user.full_name
    
    return db_obj

@router.get("/{news_id}/comments", response_model=List[Comment])
def read_comments(
    *,
    db: Session = Depends(get_db),
    news_id: int,
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Get comments for a news post.
    """
    comments = db.query(CommentModel).filter(CommentModel.news_id == news_id).offset(skip).limit(limit).all()
    
    # Enrich with author_name
    for comment in comments:
        if comment.author:
             comment.author_name = comment.author.full_name
             
    return comments

@router.post("/{news_id}/like", response_model=News)
def like_news(
    *,
    db: Session = Depends(get_db),
    news_id: int,
    current_user: UserModel = Depends(get_current_user)
) -> Any:
    """
    Like a news post.
    """
    news = crud.news.get(db, id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News post not found")
        
    # Simple increment for now. 
    # In a real app, check if user already liked it using a separate mapping table
    news.likes = (news.likes or 0) + 1
    db.add(news)
    db.commit()
    db.refresh(news)
    
    if news.author:
        news.author_name = news.author.full_name
        news.author_avatar = news.author.avatar
        
    return news
