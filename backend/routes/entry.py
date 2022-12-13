from typing import List
from fastapi import APIRouter, Depends , HTTPException ,status
from sqlalchemy.orm import Session

from ..models import entry_model, competition_model
from ..schemas import entry as entry_schema
from ..utilities.schemas import get_db

router = APIRouter(prefix="/entry",tags=['Entry'])

# Creating entery
@router.post("/",response_model=entry_schema.ShowEntry)
def create_entry(competition_id,request: entry_schema.CreateEntry,db: Session = Depends(get_db)):
    entry = entry_model.Entry(title = request.title, topic = request.topic, country=request.country,state=request.state,competition_id=competition_id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

# Displaying all enteries
@router.get("/{competition_id}", response_model=List[entry_schema.ShowEntries])
def display_entries(db: Session = Depends(get_db)):
    entries = db.query(entry_model.Entry).all()
    return entries

# Displaying specific entry based on id
@router.get("/{competition_id}/{entry_id}", response_model=entry_schema.ShowEntry)
def display_entry(entry_id, db: Session = Depends(get_db)):
    entry = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id).first()
    return entry

# Counting competition enteries
@router.get('/entry/{user_id}/count')
def count_user(user_id, db: Session = Depends(get_db)):
    competitions = db.query(competition_model.Competition.id).filter(competition_model.Competition.user_id == user_id).all()

    competitions = [competition.id for competition in competitions]
    result = 0
    for competition in competitions:
        entry = (db.query(entry_model.Entry.id).filter(entry_model.Competition.id == competition).count())
        result += entry
    return result

# Updating enteries
@router.put( "/{competition_id}/{entry_id}",response_model=entry_schema.ShowEntry)
def update_entry(entry_id,request: entry_schema.UpdateEntry,db: Session = Depends(get_db)):
    entry = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id).first()
    entry.title = request.title
    entry.topic = request.topic
    db.commit()
    db.refresh(entry)
    return entry

# Deleting entery
@router.delete("/{competition_id}/{entry_id}")
def delete_competition(entry_id, db: Session = Depends(get_db)):
   entry = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id)
   if not entry.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {entry_id} not found")

   entry.delete(synchronize_session = 'fetch')
   db.commit()
   return "entry deleted"
