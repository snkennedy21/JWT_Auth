from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas.schemas import UserCreate
from .. import utils
from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel, EmailStr

router = APIRouter(
  tags = ["Authentication"]
)

class UserModel(BaseModel):
    email: EmailStr
    password: str

# in production you can use Settings management
# from pydantic to get secret key from .env
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {'cookies', 'headers'}
    authjwt_access_cookie_key: str = 'access_token'
    authjwt_refresh_cookie_key: str = 'refresh_token'
    authjwt_cookie_csrf_protect: bool = False
    authjwt_cookie_domain: str = None
    authjwt_cookie_samesite: str = "lax"

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/login')
def login(user: UserModel, response: Response, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):

    # Check if User Exists in Database
    the_user = db.query(User).filter(User.email == user.email).first()
    if user.email != the_user.email or not utils.verify(user.password, the_user.hashed_password):
        raise HTTPException(status_code=401,detail="Bad username or password")

    # Create the tokens and passing to set_access_cookies or set_refresh_cookies
    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)

    # Set the Token Cookies in the response
    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)
    return {"msg":"Successfully login"}

@router.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

@router.get('/partially-protected')
def partially_protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_optional()

    # If no jwt is sent in the request, get_jwt_subject() will return None
    current_user = Authorize.get_jwt_subject() or "anonymous"
    return {"user": current_user}

@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):

    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}

@router.post("/user")
def create_user(new_user_data: UserCreate, db: Session = Depends(get_db)):

    # Hash The Users Password and Create a New User
    hashed_password = utils.hash(new_user_data.password)
    new_user_data.hashed_password = hashed_password
    del new_user_data.password
    new_user = User(**new_user_data.dict())

    print("HELLO")

    # Add the New User to the Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user