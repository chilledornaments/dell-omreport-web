from domsa_web import app, json_loadinator
from flask import render_template, request
from flask_mongoalchemy import MongoAlchemy
import json
"""
for i in b['Report']:
     print(b['Report'][i]['Description'])


# Get most recent item in collection
db.collection.find().sort({'_id':-1}).limit(1)
"""

@app.route('/api/report', methods=['POST'])
def report_api():
    if request.json:
        category = request['Category']


