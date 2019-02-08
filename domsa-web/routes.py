from domsa-web import app
from flask import render_template, request
from flask_mongoalchemy import MongoAlchemy
import json
"""
for i in b['Report']:
     print(b['Report'][i]['Description'])

"""

@app.route(/'api/report', methods=['POST'])
def report_api():
    if request.json:
        category = request['Category']

