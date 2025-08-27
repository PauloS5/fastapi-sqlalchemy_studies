from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

class Product(BaseModel):
    id:     int | None  = None
    name:   str
    price:  float
    count:  float       = 0

products = [
    Product(id=1, name="arroz",  price=7.8),
    Product(id=2, name="feijao", price=10),
    Product(id=3, name="batata", price=16.99)
]

app = FastAPI()

@app.get("/products/")
async def all():
    return products

@app.get("/products/{id}")
async def find(id: int = Path(ge=1)):
    for p in products:
        if p.id == id:
            return p
    return {"error": "not found"}

@app.post("/products/")
async def save(product: Product = Body(embed=True)):
    last_id = 0
    for p in products:
        last_id = max(last_id, p.id)
    products.append(Product(
        id=last_id+1, 
        name=product.name, 
        price=product.price, 
        count=product.count,
    ))
    return {"msg": "OK"}