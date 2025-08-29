from pydantic import BaseModel, Field
from fastapi import FastAPI, Body, Path

class User(BaseModel):
    id:       int | None = Field(default=None, gt=0, title="Identificado do Usuário", description="Não é obrigatório já que no cadastro o servidor deve atribuir um valor.")
    name:     str        = Field(min_length=2, max_length=200, title="Nome do Usuário", description="Nome completo do usuário.")
    age:      int        = Field(ge=18, title="Idade do Usuário", description="Deve ser maior que ou igaul 18.")
    email:    str        = Field(min_length=5, max_length=200, title="E-mail do usuário", description="E-mail que será usado para logar no sistema", examples=["exemplo@email.com"])
    password: str        = Field(min_length=8, title="Senha do usuário", description="Senha de no mínimo8 digitos")
    number:   str | str  = Field(default=None, title="Número de telefone do Usuário", description="Não Obrigatório", examples=["(00) 00000-0000"])

users_list = [
    User(id=1, name="Sócrates", age=24, email="socrates@email.com", password="12345678"),
    User(id=2, name="Paulo", age=18, email="paulo@email.com", password="40028922"),
    User(id=3, name="Tonho", age=30, email="toin@email.com", password="arrozuva", number="(11) 22222-3333")
]

app = FastAPI()

@app.get("/users/")
async def all():
    return users_list

@app.get("/users/{id}")
async def find(id: int = Path(gt=0, title="id do usuário", description="um id válido")):
    user = None
    for u in users_list:
        if u.id == id:
            user = u
            break

    if not user:
        return {"error": "id não encontrado"}
    return user

@app.post("/users/")
async def new(user: User = Body(embed=True)):
    users_list.append(user)
    return {"msg": "OK"}