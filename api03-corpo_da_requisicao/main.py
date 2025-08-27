from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str | None = None
    birth_year: int

app = FastAPI()

@app.post("/users/")
async def save_user(user: User):
    msg = ((user.name + " has ") if user.name else "You have ") + str(datetime.now().year - user.birth_year) + " old years!"
    return {
        "msg": msg
    }