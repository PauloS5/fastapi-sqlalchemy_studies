from enum import Enum
from fastapi import FastAPI 

class Gender(Enum):
    masc = "M"
    fem = "F"
    other = "O"

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "You are at root!"}

@app.get("/hello")
async def hello():
    return {"msg": "Hello People!"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"msg": f"Hello {name}!"}

@app.get("/gender/{user_gender}")
async def gender(user_gender: Gender):
    if user_gender is Gender.masc:
        return {"you": "are a man"}
    if user_gender is Gender.fem:
        return {"you": "are a womam"}
    if user_gender is Gender.other:
        return {"you": "are a thing"}