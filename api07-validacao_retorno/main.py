from fastapi import FastAPI
from pydantic import BaseModel, Field

class Book(BaseModel):
    isbn:  str | None = Field(default=None, pattern="^\\d{3}-\\d{2}-\\d{5}-\\d{2}-\\d{1}$")
    title: str
    desc:  str | None = Field(default=None)
    auth:  str

books_list = [
    Book(isbn="000-00-00000-00-0", title="Java",   desc="Um livro de Java",   auth="Um cara aí"),
    Book(isbn="111-11-11111-11-1", title="PHP",    desc="Um livro de PHP",    auth="Um outro cara aí"),
    Book(isbn="222-22-22222-22-2", title="Python", desc="Um livro de Python", auth="Um maluco aí")
]

app = FastAPI()

@app.get("/books/", response_model=list[Book])
async def all() -> any:
    return books_list

@app.post("/books/", response_model=bool)
async def new(book: Book) -> any:
    books_list.append[Book]
    return True