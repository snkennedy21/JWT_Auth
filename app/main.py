from fastapi import FastAPI
from .routers import auth
from fastapi import Request
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException


app = FastAPI()

# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(auth.router)

@app.get('/')
def root():
    return {"Message": "Changes pushed to production"}
