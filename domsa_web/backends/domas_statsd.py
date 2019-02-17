import statsd
from domsa_web import app

def report_good_metrics(server):
    s_client = statsd.StatsClient(app.config['STATSD_SERVER'], app.config['STATSD_PORT'], prefix='good')
    s_client.incr(server)
def report_bad_metrics(server):
    s_client = statsd.StatsClient(app.config['STATSD_SERVER'], app.config['STATSD_PORT'], prefix='bad')
    s_client.incr(server)