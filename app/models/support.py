from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class TicketStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class TicketPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class SupportTicket(Base):
    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject = Column(String, index=True)
    message = Column(Text)
    status = Column(Enum(TicketStatus), default=TicketStatus.OPEN)
    priority = Column(Enum(TicketPriority), default=TicketPriority.MEDIUM)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Use string for relationship to avoid circular import
    user = relationship("app.models.user.User", back_populates="tickets")
