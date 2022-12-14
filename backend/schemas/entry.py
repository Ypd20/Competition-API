from pydantic import BaseModel

""" Schema for Creating Entry. """


class CreateEntry(BaseModel):
    title: str
    topic: str
    country: str
    state: str


""" Schema for Showing Entries. """


class ShowEntries(BaseModel):
    id: int

    class Config:
        orm_mode = True


""" Schema for Showing Specific Entry. """


class ShowEntry(BaseModel):
    id: int
    title: str
    topic: str
    country: str
    state: str

    class Config:
        orm_mode = True


""" Schema for Updating Entry. """


class UpdateEntry(BaseModel):
    title: str
    topic: str

    class Config:
        orm_mode = True
