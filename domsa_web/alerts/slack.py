from domsa_web import Config
import requests, json

def alert(category, alert_message):
    headers = {'Content-Type': 'application/json'}
    message = "OMSA Warning: {}\nError message: {}".format(str(category), str(alert_message))
    