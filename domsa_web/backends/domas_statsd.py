import statsd
from domsa_web.app import config

def report_good_metrics(server):
    s_client = statsd.StatsClient(config['STATSD_SERVER'], config['STATSD_PORT'], prefix='good')
    s_client.incr(server)
def report_bad_metrics(server):
    s_client = statsd.StatsClient(config['STATSD_SERVER'], config['STATSD_PORT'], prefix='bad')
    s_client.incr(server)