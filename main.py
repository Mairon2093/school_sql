import psycopg2
import fastapi
from fastapi import Request, Response, FastAPI

database = "school_db"
user = "school"
password = "School1234*"
host = "79.174.88.238"
port = "15221"

conn = psycopg2.connect(
    database = database,
    user = user,
    password = password,
    host = host,
    port = port
)

cur = conn.cursor()
migration = ""
with open("migrations") as f:
    migration = f.read()
    cur.execute(migration)

###

app = FastAPI()

@app.get("/ping")
async def ping():
    return Response(status_code=200)

@app.post("/orders")
async def register(r : Request):
    print(await r.json())
