from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas.resource import Resource, ResourceCreate, ResourceUpdate, ResourceCategory, ResourceCategoryCreate, ResourceCategoryUpdate
from app.core.database import get_db

router = APIRouter()

# --- Resource Category Endpoints ---

@router.get("/categories", response_model=List[ResourceCategory])
def read_categories(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    return crud.resource_category.get_multi(db, skip=skip, limit=limit)

@router.post("/categories", response_model=ResourceCategory)
def create_category(
    *,
    db: Session = Depends(get_db),
    category_in: ResourceCategoryCreate
) -> Any:
    return crud.resource_category.create(db, obj_in=category_in)

@router.get("/categories/{slug}", response_model=ResourceCategory)
def read_category_by_slug(
    *,
    db: Session = Depends(get_db),
    slug: str
) -> Any:
    category = crud.resource_category.get_by_slug(db, slug=slug)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/categories/{category_id}", response_model=ResourceCategory)
def update_category(
    category_id: int,
    *,
    db: Session = Depends(get_db),
    category_in: ResourceCategoryUpdate
) -> Any:
    category = crud.resource_category.get(db, id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.resource_category.update(db, db_obj=category, obj_in=category_in)

@router.delete("/categories/{category_id}", response_model=ResourceCategory)
def delete_category(
    category_id: int,
    *,
    db: Session = Depends(get_db)
) -> Any:
    category = crud.resource_category.get(db, id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.resource_category.remove(db, id=category_id)

# --- Resource Endpoints ---

@router.get("/", response_model=List[Resource])
def read_resources(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category_id: int = None
) -> Any:
    if category_id:
        return crud.resource.get_multi_by_category(db, category_id=category_id, skip=skip, limit=limit)
    return crud.resource.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=Resource)
def create_resource(
    *,
    db: Session = Depends(get_db),
    resource_in: ResourceCreate
) -> Any:
    return crud.resource.create(db, obj_in=resource_in)

@router.get("/{resource_id}", response_model=Resource)
def read_resource(
    *,
    db: Session = Depends(get_db),
    resource_id: int
) -> Any:
    resource = crud.resource.get(db, id=resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@router.put("/{resource_id}", response_model=Resource)
def update_resource(
    *,
    db: Session = Depends(get_db),
    resource_id: int,
    resource_in: ResourceUpdate
) -> Any:
    resource = crud.resource.get(db, id=resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return crud.resource.update(db, db_obj=resource, obj_in=resource_in)

@router.delete("/{resource_id}", response_model=Resource)
def delete_resource(
    *,
    db: Session = Depends(get_db),
    resource_id: int
) -> Any:
    resource = crud.resource.get(db, id=resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return crud.resource.remove(db, id=resource_id)
