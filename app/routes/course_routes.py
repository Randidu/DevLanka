from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas.course import Course, CourseCreate, CourseUpdate
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Course])
def read_courses(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve courses.
    """
    courses = crud.course.get_multi(db, skip=skip, limit=limit)
    return courses

@router.post("/", response_model=Course)
def create_course(
    *,
    db: Session = Depends(get_db),
    course_in: CourseCreate
) -> Any:
    """
    Create new course.
    """
    course = crud.course.create(db, obj_in=course_in)
    return course

@router.get("/{course_id}", response_model=Course)
def read_course(
    *,
    db: Session = Depends(get_db),
    course_id: int
) -> Any:
    """
    Get course by ID.
    """
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=Course)
def update_course(
    *,
    db: Session = Depends(get_db),
    course_id: int,
    course_in: CourseUpdate
) -> Any:
    """
    Update a course.
    """
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course = crud.course.update(db, db_obj=course, obj_in=course_in)
    return course

@router.delete("/{course_id}", response_model=Course)
def delete_course(
    *,
    db: Session = Depends(get_db),
    course_id: int
) -> Any:
    """
    Delete a course.
    """
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course = crud.course.remove(db, id=course_id)
    return course
