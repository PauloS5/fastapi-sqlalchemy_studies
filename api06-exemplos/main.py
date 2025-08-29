from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    desc: str | None = None
    price: float
    count: int
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "foo",
                "desc": "bar",
                "price": 1.98,
                "count": 98
            }
        }
    }

app = FastAPI()

@app.get("/")
async def returner(p: Product):
    return p