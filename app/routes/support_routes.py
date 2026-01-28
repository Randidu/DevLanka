from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas.support import SupportTicket, SupportTicketCreate, SupportTicketUpdate
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[SupportTicket])
def read_tickets(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    user_id: int = None
) -> Any:
    """
    Retrieve support tickets.
    """
    if user_id:
        return crud.support.get_multi_by_user(db, user_id=user_id, skip=skip, limit=limit)
    tickets = crud.support.get_multi(db, skip=skip, limit=limit)
    return tickets

@router.post("/", response_model=SupportTicket)
def create_ticket(
    *,
    db: Session = Depends(get_db),
    ticket_in: SupportTicketCreate,
    user_id: int # In a real app, this would come from the current user dependency
) -> Any:
    """
    Create new support ticket.
    """
    # We need to inject user_id into the create logic if it's not in the schema
    # The models show user_id is a column in SupportTicket
    db_obj = crud.support.model(user_id=user_id, **ticket_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/{ticket_id}", response_model=SupportTicket)
def read_ticket(
    *,
    db: Session = Depends(get_db),
    ticket_id: int
) -> Any:
    """
    Get support ticket by ID.
    """
    ticket = crud.support.get(db, id=ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/{ticket_id}", response_model=SupportTicket)
def update_ticket(
    *,
    db: Session = Depends(get_db),
    ticket_id: int,
    ticket_in: SupportTicketUpdate
) -> Any:
    """
    Update a support ticket.
    """
    ticket = crud.support.get(db, id=ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket = crud.support.update(db, db_obj=ticket, obj_in=ticket_in)
    return ticket

@router.delete("/{ticket_id}", response_model=SupportTicket)
def delete_ticket(
    *,
    db: Session = Depends(get_db),
    ticket_id: int
) -> Any:
    """
    Delete a support ticket.
    """
    ticket = crud.support.get(db, id=ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket = crud.support.remove(db, id=ticket_id)
    return ticket
