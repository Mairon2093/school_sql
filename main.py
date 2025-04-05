import psycopg2
import fastapi
from fastapi import Request, Response, FastAPI

from commands import GETcars, POSTcar, DELEREcar, GETinfocar, PUTcar, GETdrivers, POSTdriver, GETinfodriver, PUTdriver, DELETEdriver, GETorders, POSTorders, GETinfoorder, PUTorder, DELETEorder
from commands import Car, Driver, Order

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
    return Response(200)

### 

#GETcars(conn)
@app.get("/cars/get_all_cars")
async def cars_list(r : Request):
    print(await r.json())
    GETcars(cur)

#POSTcar(conn, number, model)
@app.post("/cars/add_car")
async def car_add(r : Request):
    car = Car.load_(await r.json())
    POSTcar(cur, car.number, car.model)

#DELEREcar(conn, id)
@app.post("/cars/delete_car")
async def car_delete(r : Request):
    car = Car.load_(await r.json())
    DELETEcar(cur, car.id)
    
#GETinfocar(conn, id)
@app.get("/cars/get_info_car")
async def car_info(r : Request):
    car = Car.load_(await r.json())
    GETinfocar(cur, car.id)

#GETdrivers(conn)
@app.get("/drivers/get_all_drivers")
async def drivers_list(r : Request):
    print(await r.json())
    GETdrivers(cur)
    
#POSTdriver(conn, raiting, name)
@app.post("/drivers/add_driver")
async def driver_add(r : Request):
    driver = Driver.load_(await r.json())
    POSTdriver(cur, driver.raiting, driver.name)
    
#GETinfodriver(conn, id)
@app.get("/drivers/get_info_driver")
async def driver_info(r : Request):
    driver = Driver.load_(await r.json())
    GETinfodriver(cur, driver.id)
    
#DELETEdriver(conn, id)
@app.post("/drivers/delete_driver")
async def driver_delete(r : Request):
    driver = Driver.load_(await r.json())
    DELETEdriver(cur, driver.id)

#GETorders(conn)
@app.get("/orders/get_all_orders")
async def orders_list(r : Request):
    print(await r.json())
    GETorders(cur)
    
#POSTorders(conn, start, end, start_time, status, pass_name, car_id, driver_id)
@app.post("/orders/add_order")
async def order_add(r : Request):
    order = Order.load_(await r.json())
    POSTorders(cur, order.start, order.end, order.start_time, order.status, order.pass_name, order.car_id, order.driver_id)

#GETinfoorder(conn, id)
@app.get("/orders/get_info_order")
async def order_info(r : Request):
    order = Order.load_(await r.json())
    GETinfoorder(cur, order.id)

#DELETEorder(conn, id)
@app.post("/orders/delete_order")
async def order_delete(r : Request):
    order = Order.load_(await r.json())
    DELETEorder(cur, order.id)
