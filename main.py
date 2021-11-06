from fastapi import FastAPI, Response
import json
import datetime as dt
from random import random
from dataclasses import dataclass, field


@dataclass
class GlobalState:
    """Class for keeping track of global state"""
    default_currencies: dict = field(default_factory=dict)
    last_currencies: dict= field(default_factory=dict)
    last_updated: int = -1 # -1 because that is not a valid timeslot number

    def __post_init__(self):
        # Load a file with the default currencies
        jfile = open('currencies.json', "r", encoding="utf-8")
        self.default_currencies = json.load(jfile)  # The currencies from the json-file.
        jfile.close()

app = FastAPI()
gs = GlobalState()

"""Calculate the current timeslot of the day"""
def time_slot() -> int:
    time_slot_length = 3  # 3 minutes per timeslot

    now_hour = int(str(dt.datetime.now())[11:13])
    now_minute = int(str(dt.datetime.now())[14:16])
    current_slot = now_hour * 60 // time_slot_length + now_minute // time_slot_length
    return current_slot

"""Make new currencies based on the default currencies + a random value"""
def currencies():
    new_currencies = gs.default_currencies
    for currency in new_currencies['valutaKurser']:
        currency['rate'] = currency['rate'] + random() # return number between 0 and 1
    return new_currencies


@app.get("/")
def send_currencies():
    if time_slot() == gs.last_updated: # We are in the same time slot as the last response, so we return the last currencies
        return gs.last_currencies
    else: # We are in a new time slot, so we create and return new currencies and update the global state
        cur = currencies()
        cur['updatedAt'] = dt.datetime.now()
        gs.last_currencies = cur
        gs.last_updated = time_slot()
        return cur

