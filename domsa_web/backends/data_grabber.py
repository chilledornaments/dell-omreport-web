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

def get_processors_data(mongo_collection):
    try:
        processor_items = db[mongo_collection].find({"Category": "Processors"}, sort=[('_id', -1)]).distinct("ProcessorName")
        if not processor_items:
            processor_data = False
        elif processor_items is None:
            processor_data = False
        else:
            processor_data = {}
            for proc in processor_items:
                query = db[mongo_collection].find({'Category': 'Processors', "ProcessorName": proc}, sort=[('_id', -1)], limit=1)
                for data in query:
                    ProcessorName = data['ProcessorName']
                    MaxSpeed = data['MaxSpeed']
                    CurrentSpeed = data['CurrentSpeed']
                    Status = data['Status']
                    Threads = data['Threads']
                    Cores = data['Cores']
                    Version = data['Version']
                    Manufacturer = data['Manufacturer']
                    processor_data[proc] = {"ProcessorName": ProcessorName, "CurrentSpeed": CurrentSpeed, "Status": Status, \
                        "MaxSpeed": MaxSpeed, "Threads": Threads, "Cores": Cores, "Version": Version, "Manufacturer": Manufacturer}
            return processor_data
    
    except Exception as e:
        return str(e)
    
def get_psu_data(mongo_collection):
    try:
        psu_items = db[mongo_collection].find({"Category": "PowerSupplies"}, sort=[('_id', -1)]).distinct("Name")
        
        if not psu_items:
            return False
            
        elif psu_items is None: 
            return False
        else:
            psu_data = {}
            for psu in psu_items:
                query = db[mongo_collection].find({"Category": "PowerSupplies", "Name": psu}, sort=[('_id', -1)], limit=1)
                
                for data in query:
                    Exists = data['Detected']
                    InputRating = data['InputRating']
                    Failed = data['Failed']
                    PredictedFail = data['PredictedFail']
                    ACLost = data['ACLost']
                    FanFailed = data['FanFailed']
                    FirmwareVersion = data['FirmwareVersion']
                    ACOn = data['ACOn']
                    psu_data[psu] = {"Exists": Exists, "InputRating": InputRating, "Failed": Failed, "PredictedFail": PredictedFail, "ACLost": ACLost, \
                        "FanFailed": FanFailed, "FirmwareVersion": FirmwareVersion, "ACOn": ACOn}
            return psu_data
    except Exception as e:
        return str(e)

def get_physicaldisk_data(mongo_collection):
    try:
        pdisk_items = db[mongo_collection].find({"Category": "PhysicalDisks"}, sort=[('_id', -1)]).distinct("OID")

        if not pdisk_items:
            return False
        elif pdisk_items is None:
            return False
        else:
            pdisk_data = {}
            for disk in pdisk_items:
                query = db[mongo_collection].find({"Category": "PhysicalDisks", "OID": disk}, sort=[('_id', -1)], limit=1)

                for data in query:
                    SerialNumber = data['SerialNumber']
                    NumberPartitions = data['NumberPartitions']
                    NegotiatedSpeed = data['NegotiatedSpeed']
                    CapableSpeed = data['CapableSpeed']
                    ProductID = data['ProductID']
                    pdisk_data[disk] = {"SerialNumber": SerialNumber, "NumberPartitions": NumberPartitions, "NegotiatedSpeed": NegotiatedSpeed, \
                        "CapableSpeed": CapableSpeed, "ProductID": ProductID}
            return pdisk_data

    except Exception as e:
        return str(e)
def get_virtual_disks(mongo_collection):
    try:
        vdisk_items = db[mongo_collection].find({"Category": "VirtDisks"}, sort=[('_id', -1)]).distinct("OID")
        if not vdisk_items:
            return False
        elif vdisk_items is None:
            return False
        else:
            vdisk_data = {}
            for vdisk in vdisk_items:
                query = db[mongo_collection].find({"Category": "VirtDisks", "OID": vdisk}, sort=[('_id', -1)], limit=1)

                for data in query:
                    DeviceName = data['DeviceName']
                    PoolName = data['PoolName']
                    Status = data['Status']
                    StripeSize = data['StripeSize']

                    vdisk_data[vdisk] = {"DeviceName": DeviceName, "PoolName": PoolName, "Status": Status, "StripeSize": StripeSize}
            return vdisk_data
    except Exception as e:
        return str(e)
def get_fan_data(mongo_collection):
    try:
        fan_items = db[mongo_collection].find({"Category": "Fans"}, sort=[('_id', -1)]).distinct("Fan")
        
        if not fan_items:
            return False
        elif fan_items is None:
            return False
        else:
            fan_data = {}
            for fan in fan_items:
                query = db[mongo_collection].find({"Category": "Fans", "Fan": fan}, sort=[('_id', -1)], limit=1)

                for data in query:
                    SpeedInRPM = data['SpeedInRPM']
                    fan_data[fan] = {"Fan": fan, "SpeedInRPM": SpeedInRPM}
            return fan_data
    except Exception as e:
        return str(e)
    
def get_nic_data(mongo_collection):
    try:
        nic_items = db[mongo_collection].find({"Category": "NICs"}, sort=[('_id', -1)]).distinct("Interface")
        if not nic_items:
            return False
        elif nic_items is None:
            return False
        else:
            nic_data = {}
            for nic in nic_items:
                query = db[mongo_collection].find({"Category": "NICs", "Interface": nic}, sort=[('_id', -1)], limit=1)

                for data in query:
                    Description = data['Description']
                    Slot = data['Slot']
                    MTU = data['MTU']
                    Vendor = data['Vendor']
                    DriverVersion = data['DriverVersion']
                    FirmwareVersion = data['FirmwareVersion']
                    CurrentMAC = data['CurrentMAC']

                    nic_data[nic] = {"Description": Description, "Slot": Slot, "MTU": MTU, "Vendor": Vendor, "DriverVersion": DriverVersion, "FirmwareVersion": FirmwareVersion, "CurrentMAC": CurrentMAC}

            return nic_data
    except Exception as e:
        return str(e)