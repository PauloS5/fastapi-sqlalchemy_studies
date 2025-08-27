from enum import Enum
from fastapi import FastAPI

class Field(Enum):
    name = "name"
    age = "age"
    gender = "gender"

users_list = [
    {
        "id": 1,
        "name": "Paulo",
        "age": 10,
        "gender": "M"
    },
    {
        "id": 2,
        "name": "Anthony",
        "age": 14,
        "gender": "F"
    },
    {
        "id": 3,
        "name": "Sócrates",
        "age": 16,
        "gender": "M"
    }
]

app = FastAPI()

@app.get("/users")
async def all(field: Field|None = None):
    if field:
        users = {}
        for u in users_list:
            users[u["id"]] = u[field.name]
        return users
    return users_list

@app.get("/users/{id}")
async def find(id: int):
    if id:
        for u in users_list:
            if (u["id"] == id):
                return u
        return {"msg": "not found"}
    return users_list