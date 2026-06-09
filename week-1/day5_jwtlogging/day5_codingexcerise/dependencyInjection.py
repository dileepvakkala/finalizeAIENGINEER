from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db

app = FastAPI()

@app.get("/")
def home(
    db: Session= Depends(get_db)):
    pass
