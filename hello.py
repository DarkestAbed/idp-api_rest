# hello.py

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app: FastAPI = FastAPI(
    debug=True,
    title="API de prueba",
    version="0.0.1",
)


class UserLogin(BaseModel):
    user: str
    pswd: str
    email: EmailStr


@app.get("/")
def _():
    return {
        "message": "Hello World from my first API",
    }


@app.post("/login")
def _(payload: UserLogin):
    return {
        "message": f"user {payload.user} was successfully created",
        "details": {
            "user_name": payload.user,
            "user_email": payload.email,
            "user_password": payload.pswd,
        }
    }
