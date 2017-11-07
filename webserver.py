
import time

from flask import Flask, render_template, request


KEY_EXPIRES_SECONDS = 'expires_s'
KEY_EXPIRES_MINUTES = 'expires_m'
KEY_EXPIRES_HOURS = 'expires_h'

# DEFAULT_EXPIRATION = 10  # 10 sec
# DEFAULT_EXPIRATION = 60 * 10  # 10 min
DEFAULT_EXPIRATION = 60 * 20  # 20 min


app = Flask(__name__)


last_ping = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ping/<thing>', methods=['PUT'])
def ping_put(thing):
    now = time.time()
    last_ping[thing] = now
    return "%s %s" % (thing, now)


def _get_expiration():
    seconds = request.args.get(KEY_EXPIRES_SECONDS)
    if seconds:
        return int(seconds)
    minutes = request.args.get(KEY_EXPIRES_MINUTES)
    if minutes:
        return int(minutes) * 60
    hours = request.args.get(KEY_EXPIRES_HOURS)
    if hours:
        return int(hours) * 60 * 60
    return DEFAULT_EXPIRATION


@app.route('/ping/<thing>', methods=['GET'])
def ping_get(thing):
    if thing not in last_ping:
        response = u"No such thing as %s" % thing
        return response, 404
    elapsed = time.time() - last_ping[thing]
    expiration = _get_expiration()
    if elapsed > expiration:
        del last_ping[thing]
        response = u"Thing expired: %s" % thing
        return response, 404
    return "%s %s" % (thing, elapsed)
