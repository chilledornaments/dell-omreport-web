from domsa_web import app, client, db

def get_memory_data(mongo_collection):
    try:
        # Find each unique memory module
        memory_items = db[mongo_collection].find({"Category": "Memory"}, sort=[('_id', -1)]).distinct("Device")
        if not memory_items:
           memory_items = ["Memory Not Collected"]     
        elif memory_items is None:
            memory_items = ["Memory Not Collected"]
        else:
            
            memory_data = {}

            for device in memory_items:
                query = db[mongo_collection].find({"Category": "Memory", "Device": device}, sort=[('_id', -1)], limit=1)
                for data in query:
                    status = data['Status']
                    Manufacturer = data['Manufacturer']
                    SerialNumber = data['SerialNumber']
                    PartNumber = data['PartNumber']
                    Size = data['Size']
                    Speed = data['Speed']
                
                    memory_data[device] = {"Status": status, "Manufacturer": Manufacturer, "SerialNumber": SerialNumber, "PartNumber": PartNumber, "Size": Size, "Speed": Speed}
            
            return memory_data

    except Exception as e:
        return str(e)

def get_temperature_data(mongo_collection):
        try:
        # Find each unique memory module
            temperature_items = db[mongo_collection].find({"Category": "Temperature"}, sort=[('_id', -1)])
            if not temperature_items:
                temperature_data = False
                return temperature_data
            elif temperature_items is None:
                temperature_data = False
                return temperature_data
            else:
                temperature_data = {}
                query = db[mongo_collection].find({'Category': 'Temperature'}, sort=[('_id', -1)], limit=1)
                for data in query:
                    TempReading = data['TempReading']
                    TempInC = int(data['TempInC'])
                    temperature_data = {"TempReading": TempReading, "TempInC": TempInC}
                return temperature_data
        except Exception as e:
            return str(e)
