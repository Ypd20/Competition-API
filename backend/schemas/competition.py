from pydantic import BaseModel
from datetime import date

""" Schema for Competition. """


class CompetitionBase(BaseModel):
    name: str
    status: str
    description: str
    created_at: date
    updated_at: date
    user_id: int
    is_active: bool
    is_deleted: bool


""" Schema for Creating Competition. """


class CreateCompetition(BaseModel):
    name: str
    status: str
    description: str


""" Schema for Showing Competition. """


class ShowCompetition(BaseModel):
    name: str
    status: str
    description: str

    class Config:
        orm_mode = True


""" Schema for Updating Competition. """


class UpdateCompetition(BaseModel):
    name: str
    status: str

    class Config:
        orm_mode = True
