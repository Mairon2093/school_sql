import psycopg2
import json 

class Car:
    def __init__(self, id, car_number, car_model):
        self.id = id
        self.car_number = car_number
        self.car_model = car_model

class Driver:
    def __init__(self, id, driver_rating, driver_name):
        self.id = id
        self.driver_rating = driver_rating
        self.driver_name = driver_name

class Order:
    def __init__(self, id, start_pos, end_pos, start_time, status, passenger_name, car_id, driver_id):
        self.id = id
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.start_time = start_time
        self.status = status
        self.passenger_name = passenger_name
        self.car_id = car_id
        self.driver_id = driver_id

def GETcars():
    Korneeva = conn.cursor()
    Korneeva.execute("SELECT * FROM cars;")
    Korneeva.fetchall()

def POSTcar(number, model):
    Korneeva = conn.cursor()
    Korneeva.execute("INSERT INTO Korneeva.cars VALUES (1, "
                     + str(number) + ", " + str(model) + ");")

def DELEREcar(id):
    Korneeva = conn.cursor()
    Korneeva.execute("DELETE FROM Korneeva.cars WHERE id = " + str(id) + ";")

def GETinfocar(id):
    Korneeva = conn.cursor()
    Korneeva.execute("SELECT * FROM Korneeva.cars WHERE id = " + str(id) + ";")
    Korneeva.fetchall()

def PUTcar(id, new_model, new_number):
    Korneeva = conn.cursor()
    Korneeva.execute("UPDATE Korneeva.cars SET car_number = " + str(new_number) + ", car_model = " + str(new_model) + " WHERE id = " + str(id) + ";")

def GETdrivers():
    Korneeva = conn.cursor()
    Korneeva.execute("SELECT * FROM Korneeva.drivers;")
    Korneeva.fetchall()

def POSTdriver(raiting, name):
    Korneeva = conn.cursor()
    Korneeva.execute("INSERT INTO Korneeva.drivers VALUES (1, "
                     + str(rating) + ", " + str(name) + ");")

def GETinfodriver(id):
    Korneeva = conn.cursor()
    Korneeva.execute("SELECT * FROM Korneeva.drivers WHERE id = " + str(id) + ";")
    Korneeva.fetchall()

def PUTdriver(id, new_name, new_rate):
    Korneeva = conn.cursor()
    Korneeva.execute("UPDATE Korneeva.drivers SET driver_rating = " + str(new_rate) + ", " + "driver_name = " + str(new_name) +
                     " WHERE id = " + str(id) + ";")

def DELETEdriver(id):
    Korneeva = conn.cursor()
    Korneeva.execute("DELETE FROM Korneeva.drivers WHERE id = " + str(id) + ";")

def GETorders():
    Korneeva = conn.cursor()
    Korneeva.execute("SELECT * FROM Korneeva.orders;")
    Korneeva.fetchall()

def POSTorders(start, end, start_time, status, pass_name, car_id, driver_id):
    Korneeva = conn.cursor()
    Korneeva.execute("INSERT INTO Korneeva.orders VALUES (1, "
                     + str(start) + ", " + str(end) + ", " + str(start_time) + ", " + str(status) + ", " + str(pass_name)
                     + ", " + str(car_id) + ", " + str(driver_id) + ");")

def GETinfoorder(id):
    Korneeva = conn.cursor()
    Korneeva.execute("SELECT * FROM Korneeva.orders WHERE id = " + str(id) + ";")
    Korneeva.fetchall()

def PUTorder(id, new_status):
    Korneeva = conn.cursor()
    Korneeva.execute("UPDATE Korneeva.orders SET status = " + str(new_status) + " WHERE id = " + str(id) + ";")

def DELETEorder(id):
    Korneeva = conn.cursor()
    Korneeva.execute("DELETE FROM Korneeva.orders WHERE id = " + str(id) + ";")
