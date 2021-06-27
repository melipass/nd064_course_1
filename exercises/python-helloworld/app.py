from flask import Flask
from flask import Response
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(filename = 'app.log', level = logging.DEBUG)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/status")
def status():
    app.logger.debug('{}, status request successfull'.format(datetime.now()))
    return Response('{"result":"OK - Healthy"}', status=200, mimetype='application/json')

@app.route("/metrics")
def metrics():
    app.logger.debug('{}, metrics request successfull'.format(datetime.now()))
    return Response('{"UserCount":140,"UserCountActive":23}', status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
