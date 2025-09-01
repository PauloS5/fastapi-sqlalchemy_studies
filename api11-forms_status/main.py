from fastapi import FastAPI, Form, status, HTTPException
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(default=None)
    name: str
    email: str

users_list = [
    User(id=1,  name="Paulo Sócrates", email="socrates@email.com"),
    User(id=2,  name="Paulo Henrique", email="henrique@email.com"),
    User(id=3,  name="Paulo Tadeu",    email="tadeu@email.com"),
    User(id=4,  name="Paulo Roberto",  email="roberto@email.com"),
    User(id=5,  name="Paulo Ricardo",  email="ricardo@email.com"),
    User(id=6,  name="Paulo César",    email="cesar@email.com"),
    User(id=7,  name="Paulo Augusto",  email="augusto@email.com"),
    User(id=8,  name="Paulo Sérgio",   email="sergio@email.com"),
    User(id=9,  name="Paulo Júnior",   email="junior@email.com"),
    User(id=10, name="Paulo Almeida",  email="almeida@email.com"),
]

app = FastAPI()

@app.post("/users/", status_code=status.HTTP_201_CREATED, response_model=None)
async def save(user: User = Form()) -> any:
    last_id = 0
    for u in users_list:
        last_id = max(last_id, u.id)
    user.id = last_id+1
    users_list.append(user)

@app.get("/users/", status_code=status.HTTP_200_OK, response_model=list[User])
async def all():
    return users_list

@app.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=User)
async def find(id: int) -> any:
    user = None
    for u in users_list:
        if u.id == id:
            user = u
            break

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário inexistente!")
    return user