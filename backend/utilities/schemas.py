from ..database.database import SessionLocal

""" For connection with database."""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
