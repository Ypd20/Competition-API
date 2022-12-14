from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

""" Importing models schemas and utils. """
from ..models import competition_model
from ..schemas import competition as competition_schema
from ..utilities.schemas import get_db

router = APIRouter(prefix="/competition", tags=["Competitions"])

""" Creating Competition. """


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_competition(
    user_id,
    request: competition_schema.CreateCompetition,
    db: Session = Depends(get_db),
):
    competition = competition_model.Competition(
        name=request.name,
        status=request.status,
        description=request.description,
        user_id=user_id,
    )
    db.add(competition)
    db.commit()
    db.refresh(competition)
    return competition


""" Displaying all competitions. """


@router.get("/competitions", response_model=List[competition_schema.ShowCompetition])
def show_competitions(db: Session = Depends(get_db)):
    competitions = db.query(competition_model.Competition).all()
    return competitions


""" Displaying specific competition based on id. """


@router.get("/{competition_id}", response_model=competition_schema.ShowCompetition)
def show_competition(competition_id, db: Session = Depends(get_db)):
    competition = (
        db.query(competition_model.Competition)
        .filter(competition_model.Competition.id == competition_id)
        .first()
    )

    """ Show error if competition doesn't exist."""
    if not competition:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Competition with the id {competition_id} doesn't exist",
        )
    return competition


""" Updating Competition values. """


@router.put(
    "/update/{competition_id}", response_model=competition_schema.UpdateCompetition
)
def update_competition(
    competition_id,
    request: competition_schema.UpdateCompetition,
    db: Session = Depends(get_db),
):
    competition = (
        db.query(competition_model.Competition)
        .filter(competition_model.Competition.id == competition_id)
        .first()
    )
    competition.name = request.name
    competition.status = request.status
    db.commit()
    db.refresh(competition)
    return competition


""" Deleting Competition. """


@router.delete("/delete/{competition_id}")
def delete_competition(competition_id, db: Session = Depends(get_db)):
    competition = db.query(competition_model.Competition.id).filter(
        competition_model.Competition.id == competition_id
    )

    """ Showing error if competition doesn't exist. """
    if not competition.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Competition with id {competition_id} not found",
        )

    competition.delete(synchronize_session="fetch")
    db.commit()
    return "competition deleted"
