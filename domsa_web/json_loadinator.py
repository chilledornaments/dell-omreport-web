import json
from pymongo import MongoClient
from domsa_web import db, app
#from flask_mongoalchemy import MongoAlchemy

def Temperature(json_object):
    host = json_object['Host']
    for i in json_object['Report']: 
        TempReading = json_object['Report'][i]['TempReading']
        TempInC = json_object['Report'][i]['TempInC']
        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC}
        host_collection = db[host].insert_one(mongo_doc)
"""
def Memory(json_object):

def Processors(json_object):

def PowerSupplies(json_object):

def PhysicalDisks(json_object):

def Fans(json_object):

def NICs(json_object):

def VirtDisk(json_object):

"""