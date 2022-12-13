from pydantic import BaseModel
from datetime import date

#Classes for response_model
class CompetitionBase(BaseModel):
    name : str
    status : str
    description : str
    created_at : date
    updated_at : date
    user_id : int
    is_active : bool
    is_deleted : bool

class CreateCompetition(BaseModel):
    name : str
    status : str
    description : str



class ShowCompetition(BaseModel):
        name : str
        status : str
        description : str


        class Config():
            orm_mode = True

class UpdateCompetition(BaseModel):
    name: str
    status: str

    class Config:
        orm_mode = True
