from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/another")
def another():
    return "Another Hello World!"

@app.route("/dynamic/<name>")
def dynamic(name):
    return f"Hello {escape(name)}"