from domsa_web import app, client, db

def get_server_data(mongo_collection):
    try:
        # Find each unique memory module
        memory_items = db[mongo_collection].find({"Category": "Processors"}, sort=[('_id', -1)]).distinct("Device")
        if len(memory_items) == 0:
            memory_items = "Memory Not Collected"
        elif memory_items is None:
            memory_items = "Memory Not Collected"
        elif memory_items is "None":
            memory_items = "Memory Not Collected"
        elif not memory_items:
            memory_items = "Memory Not Collected"
        else:
            #memory_data = {}
            #for i in memory_items:
            #    dev = memory_items[i]
            #    memory_data[dev] = i
            return memory_items

    except Exception as e:
        return str(e)
