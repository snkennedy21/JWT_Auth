from typing import Union
from sqlalchemy.orm import Session
from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_db
from fastapi import Depends
from .models import User
from .schemas.schemas import UserCreate

app = FastAPI()

@app.get("/database")
def get_database(db: Session = Depends(get_db)):
    user = db.query(User).first()
    return {"name": user.first_name}

@app.get("/")
def read_root():
    return {"Hello": "Tom"}

@app.post("/user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print(user)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    