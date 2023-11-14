from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas.schemas import UserCreate
from .. import utils
from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel, EmailStr

router = APIRouter(
  tags = ["Endpoints"]
)

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

@router.get('/unprotected')
def unprotected(request: Request, Authorize: AuthJWT = Depends()):
    access_token = request.cookies.get('access_token')
    # thing = Authorize.get_raw_jwt(access_token)
    # print("THING: ", thing)
    # print("ACCESS TOKEN: ", access_token)
    return {"value": "Unprotected Page"}

@router.get('/partially-protected')
def partially_protected(Authorize: AuthJWT = Depends()):
    print("PARTIALLY PROTECTED")
    Authorize.jwt_optional()

    # If no jwt is sent in the request, get_jwt_subject() will return None
    current_user = Authorize.get_jwt_subject() or "Anonymous User"
    print("CURRENT USER: ", current_user)
    return {"user": current_user}

@router.get('/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    print("CURRENT USER: ", current_user)
    return {"user": current_user}