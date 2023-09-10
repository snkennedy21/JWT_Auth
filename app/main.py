from typing import Union
from sqlalchemy.orm import Session
from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_db
from fastapi import Depends
from .models import User
from .schemas.schemas import UserCreate
from . import utils

app = FastAPI()

@app.get("/database")
def get_database(db: Session = Depends(get_db)):
    user = db.query(User).first()
    return {"name": user.first_name}

@app.get("/")
def read_root():
    return {"Hello": "Tom"}

@app.post("/user")
def create_user(new_user_data: UserCreate, db: Session = Depends(get_db)):

    # Hash The Users Password and Create a New User
    hashed_password = utils.hash(new_user_data.password)
    new_user_data.hashed_password = hashed_password
    del new_user_data.password
    new_user = User(**new_user_data.dict())

    # Add the New User to the Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    