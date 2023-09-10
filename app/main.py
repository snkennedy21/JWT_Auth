from typing import Union
from sqlalchemy.orm import Session
from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_db
from fastapi import Depends
from .models import User
from .schemas.schemas import UserCreate, UserLogin
from . import utils
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserModel(BaseModel):
    email: EmailStr
    password: str

# in production you can use Settings management
# from pydantic to get secret key from .env
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()

# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

# provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token to use authorization
# later in endpoint protected
@app.post('/login')
def login(user: UserModel, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    the_user = db.query(User).filter(User.email == user.email).first()
    print('Hello')
    if user.email != the_user.email or not utils.verify(user.password, the_user.hashed_password):
        raise HTTPException(status_code=401,detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.email)
    return {"access_token": access_token}

# protect endpoint with function jwt_required(), which requires
# a valid access token in the request headers to access.
@app.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

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
