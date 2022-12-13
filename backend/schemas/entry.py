from pydantic import BaseModel

#Classes for response_model
class CreateEntry(BaseModel):
     title: str
     topic : str
     country : str
     state : str


class ShowEntries(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ShowEntry(BaseModel):
    id : int
    title : str
    topic : str
    country : str
    state : str

    class Config:
        orm_mode = True


class UpdateEntry(BaseModel):
    title : str
    topic : str

    class Config:
        orm_mode = True
