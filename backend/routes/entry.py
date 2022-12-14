from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

""" Importing models schemas and utils. """
from ..models import entry_model, competition_model
from ..schemas import entry as entry_schema
from ..utilities.schemas import get_db

router = APIRouter(prefix="/entry", tags=["Entry"])

""" Creating entry. """


@router.post("/", response_model=entry_schema.ShowEntry)
def create_entry(
    competition_id, request: entry_schema.CreateEntry, db: Session = Depends(get_db)
):
    entry = entry_model.Entry(
        title=request.title,
        topic=request.topic,
        country=request.country,
        state=request.state,
        competition_id=competition_id,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


""" Displaying all enteries. """


@router.get("/{competition_id}", response_model=List[entry_schema.ShowEntries])
def display_entries(db: Session = Depends(get_db)):
    entries = db.query(entry_model.Entry).all()
    return entries


""" Displaying specific entry based on id. """


@router.get("/{competition_id}/{entry_id}", response_model=entry_schema.ShowEntry)
def display_entry(entry_id, db: Session = Depends(get_db)):
    entry = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id).first()

    """ Showing error if entry doesn't exist. """
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry with the id {entry_id} doesn't exist",
        )

    return entry


""" Counting competition enteries. """


@router.get("/entry/{user_id}/count")
def count_user(user_id, db: Session = Depends(get_db)):
    competitions = (
        db.query(competition_model.Competition.id)
        .filter(competition_model.Competition.user_id == user_id)
        .all()
    )

    competitions = [competition.id for competition in competitions]
    result = 0

    for competition in competitions:
        entry = (
            db.query(entry_model.Entry.id)
            .filter(entry_model.Competition.id == competition)
            .count()
        )
        result += entry

    return result


""" Updating enteries. """


@router.put(
    "/update/{competition_id}/{entry_id}", response_model=entry_schema.ShowEntry
)
def update_entry(
    entry_id, request: entry_schema.UpdateEntry, db: Session = Depends(get_db)
):
    entry = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id)
    entry.title = request.title
    entry.topic = request.topic

    """ Showing error if entry doesn't exist. """
    if not entry.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry with id {entry_id} not found",
        )

    entry.update(request.dict())
    db.commit()

    return "updated entry"


""" Deleting entry. """


@router.delete("/delete/{competition_id}/{entry_id}")
def delete_competition(entry_id, db: Session = Depends(get_db)):
    entry = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id)

    """ Showing error if entry doesn't exist. """
    if not entry.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry with id {entry_id} not found",
        )

    entry.delete(synchronize_session="fetch")
    db.commit()

    return "entry deleted"
