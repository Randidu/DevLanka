from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.support import SupportTicket
from app.schemas.support import SupportTicketCreate, SupportTicketUpdate

class CRUDSupport(CRUDBase[SupportTicket, SupportTicketCreate, SupportTicketUpdate]):
    def get_multi_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[SupportTicket]:
        return (
            db.query(self.model)
            .filter(SupportTicket.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

support = CRUDSupport(SupportTicket)
