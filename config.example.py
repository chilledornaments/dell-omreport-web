class Config(object):
    SECRET_KEY = "a secret key that's really long and complicated"
    MONGOALCHEMY_DATABASE = ""
    MONGOALCHEMY_SERVER = ""
    MONGOALCHEMY_USER = ""
    MONGOALCHEMY_PASSWORD = ""
    MONGOALCHEMY_SERVER_AUTH = True

    SLACK = True
    SLACK_CHANNEL = ""
    SLACK_USERNAME = ""
    SLACK_ICON = ""
    SLACK_WEBHOOK = ""

    # statsd setup
    STATSD = True
    STATSD_SERVER = "localhost"
    STATSD_PORT = 8125