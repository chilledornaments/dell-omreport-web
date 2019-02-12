import json, requests

j = {}
j['Host'] = "xenserver"
j['Category'] = "Processors"
j['Report'] = {}
j['Report']['CPU1'] = {"ProcessorName": "CPU1", "MaxSpeed": "3600", "CurrentSpeed": "2133", "Manufacturer": "Intel", "Version": "Intel(R) Xeon(R) CPU           L5639  @ 2.13GHz Stepping 2", "Status": "0", "Cores": "6", "Threads": "12"}
j['Report']['CPU2'] = {"ProcessorName": "CPU2", "MaxSpeed": "3600", "CurrentSpeed": "2133", "Manufacturer": "Intel", "Version": "Intel(R) Xeon(R) CPU           L5639  @ 2.13GHz Stepping 2", "Status": "0",  "Cores": "6", "Threads": "12"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})