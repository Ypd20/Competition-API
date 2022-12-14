from pydantic import BaseModel, Field
from datetime import date

""" Schema for User. """


class User(BaseModel):
    name: str
    birth_date: date = Field(default_factory=date(2022, 12, 12))
    gender: str
    created_at: date
    updated_at: date
    is_active: bool
    is_deleted: bool


""" Schema for Creating User. """


class CreateUser(BaseModel):
    name: str
    birth_date: date = Field(default_factory=date(2022, 12, 12))
    gender: str


""" Schema for Showing User. """


class ShowUser(BaseModel):
    name: str
    birth_date: date
    gender: str

    class Config:
        orm_mode = True


""" Schema for Updating User. """


class UpdateUser(BaseModel):
    name: str
    birth_date: str

    class Config:
        orm_mode = True
