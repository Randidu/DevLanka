from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas.youtube import Tutorial, TutorialCreate, TutorialUpdate
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Tutorial])
def read_tutorials(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category: str = None
) -> Any:
    """
    Retrieve tutorials.
    """
    if category:
        return crud.tutorial.get_multi_by_category(db, category=category, skip=skip, limit=limit)
    tutorials = crud.tutorial.get_multi(db, skip=skip, limit=limit)
    return tutorials

@router.post("/", response_model=Tutorial)
def create_tutorial(
    *,
    db: Session = Depends(get_db),
    tutorial_in: TutorialCreate
) -> Any:
    """
    Create new tutorial.
    """
    tutorial = crud.tutorial.create(db, obj_in=tutorial_in)
    return tutorial

@router.get("/{tutorial_id}", response_model=Tutorial)
def read_tutorial(
    *,
    db: Session = Depends(get_db),
    tutorial_id: int
) -> Any:
    """
    Get tutorial by ID.
    """
    tutorial = crud.tutorial.get(db, id=tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return tutorial

@router.put("/{tutorial_id}", response_model=Tutorial)
def update_tutorial(
    *,
    db: Session = Depends(get_db),
    tutorial_id: int,
    tutorial_in: TutorialUpdate
) -> Any:
    """
    Update a tutorial.
    """
    tutorial = crud.tutorial.get(db, id=tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    tutorial = crud.tutorial.update(db, db_obj=tutorial, obj_in=tutorial_in)
    return tutorial

@router.delete("/{tutorial_id}", response_model=Tutorial)
def delete_tutorial(
    *,
    db: Session = Depends(get_db),
    tutorial_id: int
) -> Any:
    """
    Delete a tutorial.
    """
    tutorial = crud.tutorial.get(db, id=tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    tutorial = crud.tutorial.remove(db, id=tutorial_id)
    return tutorial
