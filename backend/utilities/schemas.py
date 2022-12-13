from ..database.database import SessionLocal
# Initialising Session
def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
        db.close()
