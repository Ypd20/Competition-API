from fastapi import FastAPI
from .routes import user, competition, entry

app = FastAPI()
""" Adding routes. """
app.include_router(user.router)
app.include_router(competition.router)
app.include_router(entry.router)
