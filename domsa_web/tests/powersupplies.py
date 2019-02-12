import json, requests

j = {}
j['Host'] = "xenserver"
j['Category'] = "PowerSupplies"
j['Report'] = {}
j['Report']['PS 1 Status'] = {"Name": "PS 1 Status", "Detected": "true", "InputRating": "7020", "Failed": "false", "PredictedFail": "false", "ACLost": "false", "FanFailed": "false", "FirmwareVersion": "00.01.32", "ACOn": "true"}
j['Report']['PS 2 Status'] = {"Name": "PS 2 Status", "Detected": "true", "InputRating": "7020", "Failed": "false", "PredictedFail": "false", "ACLost": "false", "FanFailed": "false", "FirmwareVersion": "02.08.00", "ACOn": "true"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})