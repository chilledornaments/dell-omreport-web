import json
from pymongo import MongoClient
from domsa_web import db, app, client
from domsa_web.alerts import slack
#from flask_mongoalchemy import MongoAlchemy

print(db)

def Temperature(json_object):
    host = json_object['Host']
    for i in json_object['Report']: 
        TempReading = json_object['Report'][i]['TempReading']
        TempInC = json_object['Report'][i]['TempInC']
        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC}
        host_collection = db[host].insert_one(mongo_doc)

def Memory(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                dev_location = i
                manufacturer = json_object['Report'][i]['Manufacturer']
                serial  = json_object['Report'][i]['SerialNumber']
                part_number = json_object['Report'][i]['PartNumber']
                speed = json_object['Report'][i]['Speed']
                size = json_object['Report'][i]['Size']
                status = json_object['Report'][i]['Status']
                mongo_doc = {"Host": host, "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status}
                host_collection = db[host]
                host_collection.insert(mongo_doc)
                if status != 0:
                        slack.alert("Memory", "Status is not 0 for {}".format(dev_location))


#def Processors(json_object):

def PowerSupplies(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                ac_on = json_object['Report'][i]['ACOn']
                name = json_object['Report'][i]['Name']
                #input_rating = json_object['Report'][i]['InputRating']
                fan_ok = json_object['Report'][i]['FanFailed']
                fw_ver = json_object['Report'][i]['FirmwareVersion']
                exists = json_object['Report'][i]['Detected']
                failed = json_object['Report'][i]['Failed']
                predict_fail = json_object['Report'][i]['PredictedFail']
                ac_status = json_object['Report'][i]['ACLost']
                #mongo_doc = {"Name": name, "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_ok, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                mongo_doc = {"Name": name, "Detected": exists, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_ok, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                host_collection = db[host].insert_one(mongo_doc)

"""
def PhysicalDisks(json_object):

def Fans(json_object):

def NICs(json_object):

def VirtDisk(json_object):
"""