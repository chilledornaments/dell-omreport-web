import json, requests

j = {}
j['Host'] = "xenserver"
j['Category'] = "Temperature"
j['Report'] = {}
j['Report']['System Board Ambient Temp'] = {"TempReading": "System Board Ambient Temp", "TempInC": "270"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})