from fastapi import FastAPI, status

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
async def test():
    return {"status": "OK"}

@app.post("/", status_code=status.HTTP_201_CREATED)
async def test():
    return {"status": "CREATED"}