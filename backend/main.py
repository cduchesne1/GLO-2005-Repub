from flask import Flask

app = Flask(__name__)


@app.route('/')
def heartbeat():
    return 'Hello, World!'
