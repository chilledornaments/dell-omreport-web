from domsa_web import app, json_loadinator
from domsa_web.backends import coll_finder, data_grabber
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
 
     return render_template('server_categories.html', server=server)

@app.route('/servers/<server>/memory')
def memory_summary(server):
     info = data_grabber.get_memory_data(server)
     if info is None:
          info = False
     else:
          info = info
     return render_template('memory_info.html', server=server, data=info)

@app.route('/servers/<server>/temperature')
def temp_summary(server):
     info = data_grabber.get_temperature_data(server)
     return render_template('temperature_summary.html', server=server, data=info)

@app.route('/servers/<server>/processors')
def proc_summary(server):
     info = data_grabber.get_processors_data(server)
     if info is None:
          info = False
     return render_template('processors_summary.html', server=server, data=info)

@app.route('/servers/<server>/powersupplies')
def psu_summary(server):
     info = data_grabber.get_psu_data(server)
     if info is None:
          info = False
     return render_template('psu_summary.html', server=server, data=info)

@app.route('/servers/<server>/physicaldisks')
def pdisk_summary(server):
     info = data_grabber.get_physicaldisk_data(server)
     if info is None:
          info = False
     return render_template('physical_disk_summary.html', server=server, data=info)

@app.route('/servers/<server>/virtualdisks')
def vdisk_summary(server):
     info = data_grabber.get_virtual_disks(server)
     if info is None:
          info = False
     return render_template('virtual_disk_summary.html', server=server, data=info)

@app.route('/servers/<server>/fans')
def fan_summary(server):
     info = data_grabber.get_fan_data(server)
     if info is None:
          info = False
     return render_template('fan_summary.html', server=server, data=info)

@app.route('/servers/<server>/nics')
def nic_summary(server):
     info = data_grabber.get_nic_data(server)
     if info is None:
          info = False
     print(info)
     return render_template('nic_summary.html', server=server, data=info)




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
               json_loadinator.Fans(request_json)
          elif category == "NICs":
               json_loadinator.NICs(request_json)
          elif category == "VirtDisks":
               json_loadinator.VirtDisks(request_json)
          else:
               return "Invalid Category"
          return "Passing it into a higher power"
     else:
          return "Invalid json"
     return "Hello"

