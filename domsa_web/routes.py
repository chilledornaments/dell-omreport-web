from domsa_web import app, json_loadinator
from domsa_web.backends import coll_finder
from flask import render_template, request
from flask_mongoalchemy import MongoAlchemy
import json, jsonify
"""
for i in b['Report']:
     print(b['Report'][i]['Description'])


# Get most recent item in collection
db.collection.find().sort({'_id':-1}).limit(1)
"""
@app.route('/')
def homepage():
     return render_template('homepage.html')

@app.route('/about')
def about():
     return render_template('homepage.html')

@app.route('/servers')
def server_list():
     colls = coll_finder.get_mongo_collections()
     return render_template('servers.html', colls=colls)

@app.route('/servers/<server>')
def server_summary(server):
     return server

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

