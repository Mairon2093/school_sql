import fastapi
from fastapi import Request, Response, FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return Response(200)

@app.post("/orders")
async def register(r : Request):
    print(await r.json())
