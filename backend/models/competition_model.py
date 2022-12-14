from sqlalchemy import Column, INTEGER, String, ForeignKey, BOOLEAN, DATETIME
from ..database.database import Base
from datetime import datetime
from ..models.user_model import User

""" Database Model for Entry table. """


class Competition(Base):
    __tablename__ = "competitions"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    is_active = Column(BOOLEAN, default=True)
    is_deleted = Column(BOOLEAN, default=False)
    created_at = Column(DATETIME, default=datetime.utcnow)
    updated_at = Column(DATETIME, default=datetime.utcnow)
    user_id = Column(INTEGER, ForeignKey(User.id))
