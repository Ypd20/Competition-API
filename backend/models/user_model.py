from sqlalchemy import Column, INTEGER, String,BOOLEAN,DATETIME,Date
from ..database.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    is_active = Column(BOOLEAN, default = True)
    is_deleted = Column(BOOLEAN, default = False)
    created_at = Column(DATETIME, default =datetime.utcnow)
    updated_at = Column(DATETIME, default = datetime.utcnow)
