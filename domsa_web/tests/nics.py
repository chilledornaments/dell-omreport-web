import json, requests

j = {}
j['Host'] = "xenserver"
j['Category'] = "NICs"
j['Report'] = {}
j['Report']['eth0'] = {"Name": "eth0", "Description": "PowerEdge R710 BCM5709 Gigabit Ethernet", "Slot": "Embedded", "MTU": "1500", "Vendor": "Broadcom Corporation", "DriverVersion": "2.2.5r", "FirmwareVersion": "Family 7.6.15 (7.6.15 bc 7.4.0 NCSI 2.0.11)", "CurrentMAC": "00:24:E8:6A:E7:C3"}
j['Report']['xenbr0'] = {"Name": "xenbr0", "Description": "Virtual Switch", "Slot": "Virtual", "MTU": "1500", "Vendor": "XenServer", "DriverVersion": null, "FirmwareVersion": "null", "CurrentMAC": "00:24:E8:6A:E7:C3"}

r = requests.post('http://127.0.0.1:5000/api/report', data=json.dumps(j), headers={'Content-Type': 'application/json'})