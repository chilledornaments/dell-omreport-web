from domsa_web import app, client, db

def get_server_data(mongo_collection):
    try:
        # Find each unique memory module
        memory_items = db[mongo_collection].find({"Category": "Memory"}, sort=[('_id', -1)]).distinct("Device")
        if not memory_items:
           memory_items = ["Memory Not Collected"]
        
        elif memory_items is None:
            memory_items = ["Memory Not Collected"]
        
        elif memory_items is "None":
            memory_items = ["Memory Not Collected"]
        elif type(memory_items) == "NoneType":
            memory_items = ["Memory Not Collected"]
        else:
            
            memory_data = {}

            for device in memory_items:
                query = db[mongo_collection].find({"Category": "Memory", "Device": device}, sort=[('_id', -1)], limit=1)
                for data in query:
                    status = data['Status']
                    Manufacturer = data['Manufacturer']
                    memory_data[device] = {"Status": status, "Manufacturer": Manufacturer}
            
            return memory_data

    except Exception as e:
        return str(e)
