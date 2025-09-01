from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items], summary="Find an item")
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users], summary="Find an user")
async def read_users():
    return ["Rick", "Morty"]