# hello.py

from fastapi import FastAPI
from pydantic import BaseModel


app: FastAPI = FastAPI(
    debug=True,
    title="API REST inicial",
    version="0.0.1",
)


class NewUser(BaseModel):
    user: str
    pswd: str


@app.get("/")
def _():
    return {
        "message": "Hello World from this API"
    }


@app.post("/users/create")
def _(payload: NewUser):
    return {
        "message": f"user {payload.user} created",
        "details": {
            "user_name": payload.user,
            "user_pass": payload.pswd,
        },
    }
