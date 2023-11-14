from fastapi import FastAPI, HTTPException, Depends
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
    print("Middleware executed before request")
    access_token_cookie = request.cookies.get('access_token')
    print("ACCESS TOKEN: ", access_token_cookie)
    if access_token_cookie:
        is_token_expired = check_if_access_token_expired(access_token_cookie)
        print("IS TOKEN EXPIRED ", is_token_expired)
        if is_token_expired:
            raise HTTPException(status_code=401, detail="Access token has expired")
    response = await call_next(request)
    print("Middleware executed after request")
    return response

def check_if_access_token_expired(access_token_cookie: str) -> bool:
    print("HELLO")
    decoded_token = authjwt.get_raw_jwt(access_token_cookie)
    print("DECODED TOKEN: ", decoded_token)
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
