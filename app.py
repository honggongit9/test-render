
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/alank")
def hello_alank():
    return """
    <h2>alank</h2>
    <p>hello</p>
    """