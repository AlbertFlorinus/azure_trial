from flask import Flask
from markupsafe import escape

import core

url = "https://lager.emilfolino.se/v2/products/everything"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dynamic/<name>")
def dynamic(name):
    return f"Hello {escape(name)}"

@app.route("/unique")
def give_unique():
    url = "https://lager.emilfolino.se/v2/products/everything"
    data = core.retrieve(url)["data"]
    df, _ = core.main(data)
    return core.unique(df)

@app.route("/search/<query>")
def search_for(query):
    #query.replace("_", "")
    url = "https://lager.emilfolino.se/v2/products/everything"
    data = core.retrieve(url)["data"]
    df,_ = core.main(data)
    return core.search(query, df)