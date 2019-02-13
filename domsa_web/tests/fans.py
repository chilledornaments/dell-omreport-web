import json, requests

j = {}
j['Host'] = "xenserver"
j['Category'] = "Fans"
j['Report'] = {}
j['Report']['System Board FAN 1 RPM'] = {"DeviceName": "System Board FAN 1 RPM", "SpeedInRPM": "3600"}
j['Report']['System Board FAN 3 RPM'] = {"DeviceName": "System Board FAN 3 RPM", "SpeedInRPM": "3600"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})