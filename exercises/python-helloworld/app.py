from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/status")
def status():
    return Response('{"result":"OK - Healthy"}', status=200, mimetype='application/json')

@app.route("/metrics")
def metrics():
    return Response('{"UserCount":140,"UserCountActive":23}', status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
