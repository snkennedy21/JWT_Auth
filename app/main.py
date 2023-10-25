from fastapi import FastAPI
from .routers import auth, endpoints
from fastapi import Request
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://192.168.122.163:5173',
    'http://192.168.122.163'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
