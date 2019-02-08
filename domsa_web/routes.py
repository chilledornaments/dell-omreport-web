from domsa_web import app, json_loadinator
from flask import render_template, request
from flask_mongoalchemy import MongoAlchemy
import json, jsonify
"""
for i in b['Report']:
     print(b['Report'][i]['Description'])


# Get most recent item in collection
db.collection.find().sort({'_id':-1}).limit(1)
"""

@app.route('/api/report', methods=['POST'])
def report_api():
     if request.json:
          request_json = request.json
          category = request_json['Category']

          if category == "Temperature":
               json_loadinator.Temperature(request_json)     
          elif category == "Memory":
               json_loadinator.Memory(request_json)
          elif category == "Processors":
               json_loadinator.Processors(request_json)
          elif category == "PowerSupplies":
               json_loadinator.PowerSupplies(request_json)
          elif category == "PhysicalDisks":
               json_loadinator.PhysicalDisks(request_json)
          elif category == "Fans": 
               json_loadinator.VirtDisk(request_json)
          elif category == "NICs":
               json_loadinator.NICs(request_json)
          elif category == "VirtDisk":
               json_loadinator.VirtDisk(request_json)
          else:
               return "Invalid Category"
          return "Passing it into a higher power"
     else:
          return "Invalid json"
     return "Hello"

