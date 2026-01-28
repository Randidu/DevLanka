from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas.pathway import Pathway, PathwayCreate, PathwayUpdate
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Pathway])
def read_pathways(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve pathways.
    """
    pathways = crud.pathway.get_multi(db, skip=skip, limit=limit)
    return pathways

@router.post("/", response_model=Pathway)
def create_pathway(
    *,
    db: Session = Depends(get_db),
    pathway_in: PathwayCreate
) -> Any:
    """
    Create new pathway.
    """
    pathway = crud.pathway.create(db, obj_in=pathway_in)
    return pathway

@router.get("/{slug}", response_model=Pathway)
def read_pathway_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str
) -> Any:
    """
    Get pathway by slug.
    """
    pathway = crud.pathway.get_by_slug(db, slug=slug)
    if not pathway:
        raise HTTPException(status_code=404, detail="Pathway not found")
    return pathway

@router.put("/{pathway_id}", response_model=Pathway)
def update_pathway(
    *,
    db: Session = Depends(get_db),
    pathway_id: int,
    pathway_in: PathwayUpdate
) -> Any:
    """
    Update a pathway.
    """
    pathway = crud.pathway.get(db, id=pathway_id)
    if not pathway:
        raise HTTPException(status_code=404, detail="Pathway not found")
    pathway = crud.pathway.update(db, db_obj=pathway, obj_in=pathway_in)
    return pathway

@router.delete("/{pathway_id}", response_model=Pathway)
def delete_pathway(
    *,
    db: Session = Depends(get_db),
    pathway_id: int
) -> Any:
    """
    Delete a pathway.
    """
    pathway = crud.pathway.get(db, id=pathway_id)
    if not pathway:
        raise HTTPException(status_code=404, detail="Pathway not found")
    pathway = crud.pathway.remove(db, id=pathway_id)
    return pathway
