from http import server
from pickletools import float8
import requests
import pandas as pd

def retrieve(url):
    response = requests.get(url)
    products_dict = response.json()
    return products_dict


def main(data):
    df = pd.DataFrame(data)
    df["name"] = df["name"].str.strip()
    
    #total_amount = {i.strip(): 0 for i in set(df["name"])}
    total_amount = {i:0 for i in set(df["name"])}
    error_col = []

    for i in data:
        naming = i["name"].strip()
        try:

            if i["stock"] is None:
                i["stock"] = 0

            if i["stock"] is str and all(i["stock"] in [0,1,2,3,4,5,6,7,8,9]):
                i["stock"] = int(i["stock"])
            total_amount[naming] += i["stock"]

        except:
            error_col.append(i)

    df = df.drop_duplicates(subset="name")

    for i in total_amount.keys():
        df.loc[df["name"] == i, "stock"] = total_amount[i]

    return df, error_col

def unique(df):
    x = df.iloc[:,[2,5]].copy()
    y = dict(x.transpose())
    output = {"data": [dict(i) for i in y.values()]}
    return output

def search(keyword, df):
    df = df.copy().iloc[:,[2,5]]
    x = df.loc[df["name"] == keyword]
    y = dict(x.transpose())
    output = {"data": [dict(i) for i in y.values()]}
    return output


if __name__ == "__main__":

    url = "https://lager.emilfolino.se/v2/products/everything"

    data = retrieve(url)["data"]
    df, error_col = main(data)

    datan = unique(df)
    x = search("Skruv M14", df)
    