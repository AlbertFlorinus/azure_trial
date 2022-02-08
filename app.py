from flask import Flask, jsonify, render_template
import core
import requests
import sys
import os
app = Flask(__name__)

global data_source
data_source = requests.get("https://lagerkollen.azurewebsites.net/v2/products/everything").json()["data"]

@app.route("/")
def hello_world():
    try:
        return render_template("lander.html")
    except:
        return sys.version_info

@app.route("/debug")
def test_data():
    return data_source

@app.route("/tester")
def why_not():
    return "not working"

@app.route("/unique")
def give_unique():
    df, _ = core.main(data_source)
    return jsonify(core.unique(df))

@app.route("/img_search/<path:path>")
def imsearch(path):
    df, _ = core.main(data_source)
    predictions = core.img_search(path, key)
    if predictions.status_code == 200:
        predictions = predictions.json()["tags"]
        product_classes = core.img_to_text(predictions, key)
        df = df.copy().iloc[:,[2,5]]
        output = {"data": []}
        for i in product_classes:
            x = df[df["name"].str.contains(i, case = False)]
            if len(x) > 0:
                y = x.transpose().to_dict()
                part_search = [i for i in y.values()]
                output["data"] += part_search
        output["keywords"] = product_classes
        return jsonify(output)
    else:
        return predictions.json()["message"]

@app.route("/search/<query>")
def search_for(query):
    df,_ = core.main(data_source)
    query = query.replace("_", " ")
    return jsonify(core.search(query, df))

if __name__ == "__main__":
    global key
    key = os.environ["API_KEY"]
    app.run()
