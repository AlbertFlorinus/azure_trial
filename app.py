from flask import Flask, jsonify
from itsdangerous import json
from markupsafe import escape
import core

url = "https://lager.emilfolino.se/v2/products/everything"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello_update"

@app.route("/unique")
def give_unique():
    url = "https://lager.emilfolino.se/v2/products/everything"
    data = core.retrieve(url)["data"]
    df, _ = core.main(data)
    return jsonify(core.unq(df))
    #return str(core.unique(df))

@app.route("/search/<query>")
def search_for(query):
    url = "https://lager.emilfolino.se/v2/products/everything"
    data = core.retrieve(url)["data"]
    df,_ = core.main(data)
    query = query.replace("_", " ")
    return jsonify(core.search(query, df))
    #return str(core.search(query, df))
