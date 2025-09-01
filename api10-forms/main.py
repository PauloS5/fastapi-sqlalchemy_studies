from fastapi import FastAPI, Form
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    desc: str = Field(default=None)
    count: int = Field(default=0)
    price: float

app = FastAPI()

@app.post("/products/", status_code=200)
async def create(product: Product = Form()):
    return product.model_dump()