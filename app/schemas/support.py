from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SupportTicketBase(BaseModel):
    subject: str
    message: str
    priority: Optional[str] = "medium"

class SupportTicketCreate(SupportTicketBase):
    pass

class SupportTicketUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None

class SupportTicket(SupportTicketBase):
    id: int
    user_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
