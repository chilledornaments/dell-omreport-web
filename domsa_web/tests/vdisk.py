import json, requests
j = {}
j['Host'] = "xenserver"
j['Category'] = "VirtDisks"
j['Report'] = {}
j['Report']['/dev/sda'] = {"ObjectID": "184549381", "DeviceName": "/dev/sda", "PoolName": "raidpool", "Status": "1", "StripeSize": "128"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})