from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from pymongo import MongoClient

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(Config)

client = MongoClient(app.config['MONGOALCHEMY_SERVER'], 27017)
db = app.config['MONGOALCHEMY_DATABASE']


from domsa_web import routes, json_loadinator