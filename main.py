from fastapi import FastAPI, Response
import json
import datetime as dt
from random import random
 
# Load a file with currencies

jfile = open('currencies.json', "r", encoding="utf-8")
default_currencies = json.load(jfile) # The currencies from the json-file.
jfile.close()
app = FastAPI()
last_cur = {} # the last currencies returned
last_updated = -1 # the last timeslot an update too place 

# Time between currency updates (in minutes)
time_slot_length = 3 # 3 minutes per timeslot 


"""Calculate the current timeslot of the day"""
def time_slot() -> int:
    now_hour = int(str(dt.datetime.now())[11:13])
    now_minute = int(str(dt.datetime.now())[14:16])
    current_slot = now_hour * 60 // time_slot_length + now_minute // time_slot_length
    return current_slot


"""Make new currencies based on the default currencies + a random value"""
def currencies():
    new_currencies = default_currencies
    for currency in new_currencies['valutaKurser']:
        currency['rate'] = currency['rate'] + random()
    return new_currencies
 

@app.get("/")
def send_currencies():
    global last_updated
    global last_cur
    if time_slot() == last_updated:
        return last_cur # We are in the same time slot as the last response, so we return the last currencies
    else:
        cur = currencies()
        cur['updatedAt'] = dt.datetime.now()
        last_cur = cur
        last_updated = time_slot()
        return cur