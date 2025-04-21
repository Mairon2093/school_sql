import psycopg2
import fastapi
import requests
import json

from fastapi import Request, Response, FastAPI

from main.py import conn

database = "school_db"
user = "school"
password = "School1234*"
host = "79.174.88.238"
port = "15221"

def create_car():
    car = {"car_number" : "123Ee", "car_model" : "pupupu"}
    url = f"http://{host}/cars/”
    r = requests.post(url, data=car)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.text == "Ok"

def create_driver():
    driver = {"driver_rating" : 5, "driver_name" : "chel"}
    url = f"http://{host}/drivers/”
    r = requests.post(url, data=driver)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.text == "Ok"

def create_order():
    order = {"start_pos" : "pos1", "end_pos" : "pos2", "start_time" : "12.12.2025", "status" : "completed"}
    url = f"http://{host}/orders/”
    r = requests.post(url, data=order)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.text == "Ok"

def get_car():
    car_ex = {"car_number" : "123Ee", "car_model" : "pupupu"}
    url = f"http://{host}/cars/1”
    r = requests.get(url)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    car = json.loads(r.data)
    assert car_ex == car
    

def get_driver():
    driver_ex = {"driver_rating" : 5, "driver_name" : "chel"}
    url = f"http://{host}/drivers/1”
    r = requests.get(url)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    driver = json.loads(r.data)
    assert driver_ex == driver

def get_order():
    order_ex = {"start_pos" : "pos1", "end_pos" : "pos2", "start_time" : "12.12.2025", "status" : "completed"}
    url = f"http://{host}/orders/1”
    r = requests.get(url)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    order = json.loads(r.data)
    assert order_ex == order
