from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas.schemas import UserCreate
from .. import utils
from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel, EmailStr
import os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES", 1440))

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

    # Create the access_token and refresh_token
    access_token = Authorize.create_access_token(subject=user.email)
    refresh_token = Authorize.create_refresh_token(subject=user.email)

    print("ACCESS TOKEN: ", access_token)

    # Set the Token Cookies in the response
    response.set_cookie(
        key="access_token", 
        value=access_token, 
        expires=ACCESS_TOKEN_EXPIRE_MINUTES, 
        httponly=True, 
        secure=True, 
        samesite="none"
    )
    response.set_cookie(
        key="refresh_token", 
        value=refresh_token, 
        expires=REFRESH_TOKEN_EXPIRE_MINUTES, 
        httponly=True, 
        secure=True, 
        samesite="none"
    )

    # Remove Sensitive User Data From Return Object
    del the_user.hashed_password
    del the_user.created_at
    
    return {"user": the_user}

@router.delete('/logout')
def logout(response: Response, Authorize: AuthJWT = Depends()):
    response.set_cookie(key="access_token", value="", expires=-1, httponly=True, secure=True, samesite="none")
    response.set_cookie(key="refresh_token", value="", expires=-1, httponly=True, secure=True, samesite="none")
    return {"message": "logout successful"}

@router.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}


@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):

    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    response.set_cookie(key="access_token", value=new_access_token, expires=120, httponly=True, secure=True, samesite="none")
    return {"Message": "Token Refreshed"}

@router.post("/user")
def create_user(response: Response, new_user_data: UserCreate, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):

    # Hash The Users Password and Create a New User
    hashed_password = utils.hash(new_user_data.password)
    new_user_data.hashed_password = hashed_password
    del new_user_data.password
    new_user = User(**new_user_data.dict())

    # Add the New User to the Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create the tokens and passing to set_access_cookies or set_refresh_cookies
    access_token = Authorize.create_access_token(subject=new_user.email)
    refresh_token = Authorize.create_refresh_token(subject=new_user.email)

    # Set the Token Cookies in the response
    response.set_cookie(
        key="access_token", 
        value=access_token, 
        expires=ACCESS_TOKEN_EXPIRE_MINUTES, 
        httponly=True, 
        secure=True, 
        samesite="none"
    )
    response.set_cookie(
        key="refresh_token", 
        value=refresh_token, 
        expires=REFRESH_TOKEN_EXPIRE_MINUTES, 
        httponly=True, 
        secure=True, 
        samesite="none"
    )
    return {"user": new_user}

@router.get("/check")
def check_if_user_is_logged_in(request: Request, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    access_token = request.cookies.get('access_token')
    refresh_token = request.cookies.get('refresh_token')
    print("REFRESH TOKEN: ", refresh_token)
    print("ACCESS TOKEN: ", access_token)
    if not access_token and refresh_token:
        raise HTTPException(status_code=401, detail="Expired Token")
    Authorize.jwt_optional()

    # Get the current User based on the email
    current_user_email = Authorize.get_jwt_subject() or "Anonymous User"

    if current_user_email == "Anonymous User":
        return False

    current_user = db.query(User).filter(User.email == current_user_email).first()

    # Remove Sensitive User Data From Return Object
    del current_user.hashed_password
    del current_user.created_at

    return {"user": current_user}