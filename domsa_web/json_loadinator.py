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
        TempInC = int(TempInC) / 10
        host_collection = db[host]
        if TempInC > 42.0 or TempInC < 8.0:
                alert_search = host_collection.find({'Category': 'Temperature'}, sort=[('_id', -1)], limit=1)
                if alert_search.count() == 0:
                        slack_alert_message = "Board on {} is {} degrees celsius".format(host, str(TempInC))
                        slack.alert("Temperature", slack_alert_message)
                        mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                        host_collection.insert(mongo_doc)
                else:
                        for item in alert_search:
                                try:
                                        if item['Alert'] == "False":
                                                slack_alert_message = "Board on {} is {} degrees celsius".format(host, str(TempInC))
                                                slack.alert("Temperature", slack_alert_message)
                                                mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                                                host_collection.insert(mongo_doc)
                                        else:
                                                mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "True"}
                                                host_collection.insert(mongo_doc)
                                except Exception as e:
                                        print(str(e))
                                        #mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "False"}
                                        #host_collection.insert(mongo_doc)
        else:
                mongo_doc = {"Host": host, "Category": "Temperature", "TempReading": TempReading, "TempInC": TempInC, "Alert": "False"}
                host_collection.insert(mongo_doc)

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
                host_collection = db[host]
                if status != "0":    
                        alert_search = host_collection.find({"Category": "Memory", "Device": i}, sort=[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "Status is not 0 for {} in {}".format(dev_location, host)
                                slack.alert("Memory", slack_alert_message)
                                # This document doesn't exist yet, create it
                                mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                for item in alert_search:

                                        try:
                                                if item['Alert'] == "False":
                                                        slack_alert_message = "Status is not 0 for {} in {}".format(dev_location, host)
                                                        slack.alert("Memory", slack_alert_message)
                                                        mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                else:
                                                        mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                        except Exception as e:
                                                return str(e)
                                                #mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "False"}
                                                #host_collection.insert(mongo_doc)
                                        
                                
                else:
                        mongo_doc = {"Host": host, "Category": "Memory", "Device": dev_location, "Manufacturer": manufacturer, "SerialNumber": serial, "PartNumber": part_number, "Speed": speed, "Size": size, "Status": status, "Alert": "False"}
                        host_collection.insert(mongo_doc)


def Processors(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                proc_name = json_object['Report'][i]['ProcessorName']
                max_speed = json_object['Report'][i]['MaxSpeed']
                curr_speed = json_object['Report'][i]['CurrentSpeed']
                status = json_object['Report'][i]['Status']
                manufacturer = json_object['Report'][i]['Manufacturer']
                version = json_object['Report'][i]['Version']
                cores = json_object['Report'][i]['Cores']
                thread_count = json_object['Report'][i]['Threads']

                host_collection = db[host]

                if status != "0":
                        alert_search = host_collection.find({"Category": "Processors", "Device": proc_name}, sort=[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "Status is not 0 for {} in {}".format(proc_name, host)
                                slack.alert("Processors", slack_alert_message)
                                mongo_doc = {"ProcessorName": proc_name, "Category": "Processors", "MaxSpeed": max_speed, "CurrentSpeed": curr_speed, "Status": status, \
                                        "Manufacturer": manufacturer, "Version": version, "Cores": cores, "Threads": thread_count, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                for item in alert_search:
                                        if item['Alert'] == "False":
                                                try:
                                                        slack_alert_message = "Status is not 0 for {} in {}".format(proc_name, host)
                                                        slack.alert("Processors", slack_alert_message)
                                                        mongo_doc = {"ProcessorName": proc_name, "Category": "Processors", "MaxSpeed": max_speed, "CurrentSpeed": curr_speed, "Status": status, "Manufacturer": manufacturer, \
                                                                "Version": version, "Cores": cores, "Threads": thread_count, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                except Exception as e:
                                                        return str(e)
                                        else:
                                                # Keep alert status set to true
                                                mongo_doc = {"ProcessorName": proc_name, "Category": "Processors", "MaxSpeed": max_speed, "CurrentSpeed": curr_speed, "Status": status, "Manufacturer": manufacturer, \
                                                        "Version": version, "Cores": cores, "Threads": thread_count, "Alert": "True"}
                                                host_collection.insert(mongo_doc)


                else:
                        mongo_doc = {"ProcessorName": proc_name, "Category": "Processors", "MaxSpeed": max_speed, "CurrentSpeed": curr_speed, "Status": status, "Manufacturer": manufacturer, \
                                "Version": version, "Cores": cores, "Threads": thread_count, "Alert": "False"}
                        host_collection.insert(mongo_doc)


def PowerSupplies(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                ac_on = json_object['Report'][i]['ACOn']
                name = json_object['Report'][i]['Name']
                input_rating = json_object['Report'][i]['InputRating']
                fan_failed = json_object['Report'][i]['FanFailed']
                fw_ver = json_object['Report'][i]['FirmwareVersion']
                exists = json_object['Report'][i]['Detected']
                failed = json_object['Report'][i]['Failed']
                predict_fail = json_object['Report'][i]['PredictedFail']
                ac_status = json_object['Report'][i]['ACLost']
                
                
                host_collection = db[host]

                if fan_failed == "true":
                        alert_search = host_collection.find({"Category": "PowerSupplies", "Name": name}, sort=[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "Fan {} failed on {}".format(name, host)
                                slack.alert("PowerSupplies", slack_alert_message)
                                mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                try:
                                        for item in alert_search:
                                                if item['Alert'] == "False":
                                                        slack_alert_message = "Fan on {} failed on {}".format(name, host)
                                                        slack.alert("PowerSupplies", slack_alert_message)
                                                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                else:
                                                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                except Exception as e:
                                        print(str(e))
                                        

                elif failed == "true":
                        alert_search = host_collection.find({"Category": "PowerSupplies", "Name": name}, sort[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "PowerSupply {} failed on {}".format(name, host)
                                slack.alert("PowerSupplies", slack_alert_message)
                                mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                try:
                                        for item in alert_search:
                                                if item['Alert'] == "False":
                                                        slack_alert_message = "PowerSupply {} failed on {}".format(name, host)
                                                        slack.alert("PowerSupplies", slack_alert_message)
                                                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                else:
                                                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                except Exception as e:
                                        print(str(e))
                elif predict_fail == "true":
                        alert_search = host_collection.find({"Category": "PowerSupplies", "Name": name}, sort[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "PowerSupply {} predicted to fail on {}".format(name, host)
                                slack.alert("PowerSupplies", slack_alert_message)
                                mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                try:
                                        for item in alert_search:
                                                if item['Alert'] == "False":
                                                        slack_alert_message = "PowerSupply {} predicted to fail on {}".format(name, host)
                                                        slack.alert("PowerSupplies", slack_alert_message)
                                                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                else:
                                                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                except Exception as e:
                                        print(str(e))
                
                else:
                        mongo_doc = {"Name": name, "Category": "PowerSupplies", "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on, "Alert": "False"}
                        host_collection.insert(mongo_doc)


                mongo_doc = {"Name": name, "Detected": exists, "InputRating": input_rating, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_failed, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                #mongo_doc = {"Name": name, "Detected": exists, "Failed": failed, "PredictedFail": predict_fail, "ACLost": ac_status, "FanFailed": fan_ok, "FirmwareVersion": fw_ver, "ACOn": ac_on}
                host_collection = db[host].insert(mongo_doc)


def PhysicalDisks(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                oid = json_object['Report'][i]['ObjectID']
                serial = json_object['Report'][i]['Serial']
                num_partitions = json_object['Report'][i]['NumPartitions']
                neg_speed = json_object['Report'][i]['NegotiatedSpeed']
                capable_speed = json_object['Report'][i]['CapableSpeed']
                product_id = json_object['Report'][i]['ProductID']
                status = json_object['Report'][i]['Status']
                
                host_collection = db[host]

                if status != "3":
                        alert_search = host_collection.find({"Category": "PhysicalDisks", "Name": oid}, sort=[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "Disk issue on {}. Host: {}".format(oid, host)
                                slack.alert("PhysicalDisks", slack_alert_message)
                                mongo_doc = {"OID": oid, "Category": "PhysicalDisks", "SerialNumber": serial, "NumberPartitions": num_partitions, "NegotiatedSpeed": neg_speed, "CapableSpeed": capable_speed, "ProductID": product_id, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                try:
                                        for item in alert_search:
                                                if item['Alert'] == "False":
                                                        slack_alert_message = "Disk issue on {}. Host: {}".format(oid, host)
                                                        slack.alert("PhysicalDisks", slack_alert_message)
                                                        mongo_doc = {"OID": oid, "Category": "PhysicalDisks", "SerialNumber": serial, "NumberPartitions": num_partitions, "NegotiatedSpeed": neg_speed, "CapableSpeed": capable_speed, "ProductID": product_id, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                else:
                                                        mongo_doc = {"OID": oid, "Category": "PhysicalDisks", "SerialNumber": serial, "NumberPartitions": num_partitions, "NegotiatedSpeed": neg_speed, "CapableSpeed": capable_speed, "ProductID": product_id, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                except Exception as e:
                                        print(str(e))
                else:
                        mongo_doc = {"OID": oid, "Category": "PhysicalDisks", "SerialNumber": serial, "NumberPartitions": num_partitions, "NegotiatedSpeed": neg_speed, "CapableSpeed": capable_speed, "ProductID": product_id, "Alert": "False"}
                        host_collection.insert(mongo_doc)



def Fans(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                host_collection = db[host]

                SpeedInRPM = json_object['Report'][i]['SpeedInRPM']
                mongo_doc = {"Category": "Fans", "SpeedInRPM": SpeedInRPM, "Fan": i, "Alert": "False"}
                host_collection.insert(mongo_doc)

def VirtDisks(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                host_collection = db[host]

                ObjectID = json_object['Report'][i]['ObjectID']
                DeviceName = json_object['Report'][i]['DeviceName']
                PoolName = json_object['Report'][i]['PoolName']
                Status = json_object['Report'][i]['Status']
                StripeSize = json_object['Report'][i]['StripeSize']
                if Status != "1":
                        alert_search = host_collection.find({"Category": "VirtDisks", "Name": ObjectID}, sort=[('_id', -1)], limit=1)
                        if alert_search.count() == 0:
                                slack_alert_message = "Virtual Disk issue on {}. Host: {}".format(DeviceName, host)
                                slack.alert("VirtDisks", slack_alert_message)
                                mongo_doc = {"OID": ObjectID, "Category": "VirtDisks", "DeviceName": DeviceName, "PoolName": PoolName, "Status": Status, "StripeSize": StripeSize, "Alert": "True"}
                                host_collection.insert(mongo_doc)
                        else:
                                try:
                                        for item in alert_search:
                                                if item['Alert'] == "False":
                                                        slack_alert_message = "Virtual Disk issue on {}. Host: {}".format(DeviceName, host)
                                                        slack.alert("VirtDisks", slack_alert_message)
                                                        mongo_doc = {"OID": ObjectID, "Category": "VirtDisks", "DeviceName": DeviceName, "PoolName": PoolName, "Status": Status, "StripeSize": StripeSize, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                                else:
                                                        mongo_doc = {"OID": ObjectID, "Category": "VirtDisks", "DeviceName": DeviceName, "PoolName": PoolName, "Status": Status, "StripeSize": StripeSize, "Alert": "True"}
                                                        host_collection.insert(mongo_doc)
                                except Exception as e:
                                        print(str(e))

                else:
                        mongo_doc = {"Category": "VirtDisks", "OID": ObjectID, "DeviceName": DeviceName, "PoolName": PoolName, "Status": Status, "StripeSize": StripeSize, "Alert": "False"}
                        host_collection.insert(mongo_doc) 

def NICs(json_object):
        host = json_object['Host']
        for i in json_object['Report']:
                host_collection = db[host]
                
                Interface = i
                Description = json_object['Report'][i]['Description']
                Slot = json_object['Report'][i]['Slot']
                MTU = json_object['Report'][i]['MTU']
                Vendor = json_object['Report'][i]['Vendor']
                DriverVersion = json_object['Report'][i]['DriverVersion']
                FirmwareVersion = json_object['Report'][i]['FirmwareVersion']
                CurrentMAC = json_object['Report'][i]['CurrentMAC']

                mongo_doc = {"Category": "NICs", "Interface": Interface, "Description": Description, "Slot": Slot, "MTU": MTU, "Vendor": Vendor, "DriverVersion": DriverVersion, \
                        "FirmwareVersion": FirmwareVersion, "CurrentMAC": CurrentMAC, "Alert": "False"}
                host_collection.insert(mongo_doc)

