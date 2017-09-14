
import time

from flask import Flask, render_template


# DEFAULT_EXPIRATION = 10  # 10 sec
DEFAULT_EXPIRATION = 60 * 10  # 10 min


app = Flask(__name__)


last_ping = {}


@app.route('/')
def index():
    # return 'Hello, World!'
    return render_template('index.html')


@app.route('/ping/<thing>')
def ping(thing):
    now = time.time()
    last_ping[thing] = now
    return "%s %s" % (thing, now)


@app.route('/check/<thing>')
def check(thing):
    if thing not in last_ping:
        response = u"No such thing as %s" % thing
        return response, 404
    elapsed = time.time() - last_ping[thing]
    if elapsed > DEFAULT_EXPIRATION:
        del last_ping[thing]
        response = u"Thing expired: %s" % thing
        return response, 404
    return "%s %s" % (thing, elapsed)
