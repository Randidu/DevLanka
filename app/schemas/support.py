from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# --- REPLY SCHEMAS ---
class TicketReplyBase(BaseModel):
    message: str

class TicketReplyCreate(TicketReplyBase):
    pass

class TicketReply(TicketReplyBase):
    id: int
    ticket_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- TICKET SCHEMAS ---
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
    replies: List[TicketReply] = []

    class Config:
        from_attributes = True
