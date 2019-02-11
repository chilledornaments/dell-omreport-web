from domsa_web import app
import requests, json

def alert(category, alert_message):
    headers = {'Content-Type': 'application/json'}
    messsage = "OMSA Warning: {}\nError message: {}".format(str(category), str(alert_message))
    json_data = {}
    json_data['channel'] = app.config['SLACK_CHANNEL']
    json_data['icon_emoji'] = app.config['SLACK_ICON']
    json_data['username'] = app.config['SLACK_USERNAME']
    json_data['attachments'] = [{
        'title': "OMSA Alert",
        'color': 'danger',
        'fallback': 'OMSA Alert',
        'text': messsage
    }]

    try:
        requests.post(app.config['SLACK_WEBHOOK'], data=json.dumps(json_data), headers=headers)
    except Exception as e:
        print(str(e))
