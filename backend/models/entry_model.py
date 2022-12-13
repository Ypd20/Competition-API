from sqlalchemy import Column, INTEGER, String, ForeignKey,BOOLEAN,DATETIME
from ..database.database import Base
from datetime import datetime
from ..models.competition_model import Competition

class Entry(Base):
    __tablename__ = "entry"
    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String)
    topic = Column(String)
    country = Column(String)
    state = Column(String)
    is_active = Column(BOOLEAN, default = True)
    is_deleted = Column(BOOLEAN, default = False)
    created_at = Column(DATETIME, default =datetime.utcnow)
    updated_at = Column(DATETIME, default = datetime.utcnow)
    competition_id = Column(INTEGER, ForeignKey(Competition.id), nullable=False)
