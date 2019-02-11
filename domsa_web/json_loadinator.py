import json
from pymongo import MongoClient
from domsa_web import db, app, client
from domsa_web.alerts import slack
#from flask_mongoalchemy import MongoAlchemy

def Temperature(json_object):
    host = json_object['Host']
    for i in json_object['Report']: 
        TempReading = json_object['Report'][i]['TempReading']
        TempInC = json_object['Report'][i]['TempInC']
        TempInC = TempInC / 10
        #mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "False"}
        host_collection = db[host]
        #inserted_id = host_collection.insert_one(mongo_doc).inserted_id
        if TempInC > 42.0:
                alert_search = host_collection.find({'Category': 'Temperature'}).sort({'_id':-1}).limit(1)
                if alert_search['Alert'] == "False":
                        slack.alert("Temperature", "Board on {} is {} degrees celsius".format(host, str(TempInC)))
                        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                        inserted_id = host_collection.insert_one(mongo_doc).inserted_id
                else:
                        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                        inserted_id = host_collection.insert_one(mongo_doc).inserted_id
        elif TempInC < 8.0:
                alert_search = host_collection.find({'Category': 'Temperature'}).sort({'_id':-1}).limit(1)
                if alert_search['Alert'] == "False":
                        slack.alert("Temperature", "Board on {} is {} degrees celsius".format(host, str(TempInC)))
                        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                        inserted_id = host_collection.insert_one(mongo_doc).inserted_id
                else:
                        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                        inserted_id = host_collection.insert_one(mongo_doc).inserted_id
        else:
                mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "False"}
                inserted_id = host_collection.insert_one(mongo_doc).inserted_id

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
                #mongo_doc = {"Host": host, "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status}
                host_collection = db[host]
                #inserted_id = host_collection.insert_one(mongo_doc).inserted_id
                if status != "0":
                        
                        #alert_search = host_collection.find_one([{"Category": "Memory"}, {"Host": host}, {"Device": i}], sort=[('_id', -1)])#.limit(1)
                        alert_search = host_collection.find({"Category": "Memory", "Device": i}, sort=[('_id', -1)], limit=1)
                        #print(alert_search)
                        for item in alert_search:
                       
                                try:
                                        #alert_search = host_collection.find_one([{"Category": "Memory"}, {"Host": host}, {"Device": i}], sort=[('_id', -1)])#.limit(1)
                                        
                                        
                                        
                                        if item['Alert'] == "False":
                                                slack_alert_message = "Memory", "Status is not 0 for {} in {}".format(dev_location, host)

                                                slack.alert("Memory", slack_alert_message)
                                                mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "True"}
                                                host_collection.insert(mongo_doc)
                                        else:
                                                mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "True"}
                                                host_collection.insert(mongo_doc)
                                except TypeError as e:
                                        mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "False"}
                                        host_collection.insert(mongo_doc)
                                        print(str(e))
                                
                else:
                        mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "False"}
                        host_collection.insert(mongo_doc)


#def Processors(json_object):

def PowerSupplies(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                ac_on = json_object['Report'][i]['ACOn']
                name = json_object['Report'][i]['Name']
                input_rating = json_object['Report'][i]['InputRating']
                fan_ok = json_object['Report'][i]['FanFailed']
                fw_ver = json_object['Report'][i]['FirmwareVersion']
                exists = json_object['Report'][i]['Detected']
                failed = json_object['Report'][i]['Failed']
                predict_fail = json_object['Report'][i]['PredictedFail']
                ac_status = json_object['Report'][i]['ACLost']
                mongo_doc = {"Name": name, "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_ok, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                #mongo_doc = {"Name": name, "Detected": exists, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_ok, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                host_collection = db[host].insert_one(mongo_doc)

"""
def PhysicalDisks(json_object):

def Fans(json_object):

def NICs(json_object):

def VirtDisk(json_object):
"""