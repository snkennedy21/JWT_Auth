from typing import Union
from sqlalchemy.orm import Session
from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_db
from fastapi import Depends
from .models import User

from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.exc import OperationalError

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>:<database port>/<database_name>"
SQLALCHEMY_DATABASE_URL = f'postgresql://root:root@db:5432/test_db'

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/database")
def get_database(db: Session = Depends(get_db)):
    user = db.query(User).first()
    return {"name": user.name}

@app.get("/")
def read_root():
    return {"Hello": "Tom"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}