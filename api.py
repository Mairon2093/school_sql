import fastapi

app = FastAPI()

@app.get("/ping")
async def ping():
    return Response(200)

@app.post("/orders")
async def register(r: Request):
    body = await RegUserModel.load(r.json())
    print(body)
