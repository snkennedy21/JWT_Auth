from fastapi import FastAPI, HTTPException, Depends, Response
from .routers import auth, endpoints
from fastapi import Request
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
import jwt
from datetime import datetime

app = FastAPI()

origins = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

authjwt = AuthJWT()

async def before_request_middleware(request: Request, call_next):
    access_token = request.cookies.get('access_token')
    refresh_token = request.cookies.get('refresh_token')
    response = await call_next(request)
    if access_token:
        is_token_expired = check_if_access_token_expired(access_token)
        if is_token_expired:
            raise HTTPException(status_code=401, detail="Access token has expired")

    if not access_token and refresh_token:
        decoded_refresh_token = authjwt.get_raw_jwt(refresh_token)
        new_access_token = authjwt.create_access_token(subject=decoded_refresh_token.get("sub"))
        new_refresh_token = authjwt.create_refresh_token(subject=decoded_refresh_token.get("sub"))
        response.set_cookie(key="access_token", value=new_access_token, expires=60, httponly=True, secure=True, samesite="none")
        response.set_cookie(key="refresh_token", value=new_refresh_token, expires=86400, httponly=True, secure=True, samesite="none")
    return response

def check_if_access_token_expired(access_token: str) -> bool:
    decoded_token = authjwt.get_raw_jwt(access_token)
    expiration_time = decoded_token.get('exp', 0) * 1000
    current_time = datetime.utcnow().timestamp() * 1000
    return current_time > expiration_time

# Register the middleware
app.middleware("http")(before_request_middleware)

# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(auth.router)
app.include_router(endpoints.router)

@app.get('/')
def root():
    return {"Message": "Hello World"}
