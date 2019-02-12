import json, requests

j = {}
j['Host'] = "xenserver"
j['Category'] = "PowerSupplies"
j['Report'] = {}
j['Report']['184549383'] = {"ProductID": "WDC WD2000F9YZ-09N20L1", "ObjectID": "184549383", "Serial": "WD-WMC160D09D4A", "NumPartitions": "1", "NegotiatedSpeed": "6144", "CapableSpeed": "6144", "Status": "3"}
j['Report']['184549383'] = {"ProductID": "WDC WD2004FBYZ-01YCBB1", "ObjectID": "184549384", "Serial": "WD-WMC6N0D9D5VV", "NumPartitions": "1", "NegotiatedSpeed": "6144", "CapableSpeed": "6144", "Status": "3"}
j['Report']['184549383'] = {"ProductID": "WDC WD2004FBYZ-01YCBB1", "ObjectID": "184549385", "Serial": "WD-WMC6N0D4NKZ2", "NumPartitions": "1", "NegotiatedSpeed": "6144", "CapableSpeed": "6144", "Status": "3"}
j['Report']['184549383'] = {"ProductID": "WDC WD2000F9YZ-09N20L1", "ObjectID": "184549386", "Serial": "WD-WMC5C0D9XDFD", "NumPartitions": "1", "NegotiatedSpeed": "6144", "CapableSpeed": "6144", "Status": "3"}



r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})