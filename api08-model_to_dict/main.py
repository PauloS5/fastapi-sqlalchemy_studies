from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
    heigth: float

talita = User(name="Tácito", email="talita@email.com", age=14, heigth=1.50)

print(talita)
print(talita.model_dump())