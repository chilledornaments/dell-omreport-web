import json

j = {}
j['Host'] = "xenserver2"
j['Category'] = "Memory"
j['Report'] = {}
j['Report']['DIMM_A1'] = {"Manufacturer": "Micron Technology (002C00B3802C)", "SerialNumber": "D75958FA", "PartNumber": "36JSZF1G72PZ-1G4D1", "Speed": "1333", "Size": "8388608", "Status": "0"}
j['Report']['DIMM_B3'] = {"Manufacturer": "Micron Technology (002C00B3802C)", "SerialNumber": "DD70B4C2", "PartNumber": "36JSZF1G72PZ-1G4D1", "Speed": "1333", "Size": "8388608", "Status": "0"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})