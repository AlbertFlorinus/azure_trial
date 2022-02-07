import requests
import pandas as pd

def img_search(url, key):
    api = 'https://dv1615-apimanagement-lab.azure-api.net/vision/v2.0/analyze?visualFeatures=Tags'
    body = {"url": url}
    headers = {'Ocp-Apim-Subscription-Key': key}
    response = requests.post(api, headers =headers, json=body)
    return response

def img_to_text(img_resp, key):
    api = "https://dv1615-apimanagement-lab.azure-api.net/translate?api-version=3.0&from=en&to=sv"
    body = [{"text": i["name"]} for i in img_resp]
    headers = {'Ocp-Apim-Subscription-Key': key}
    response = requests.post(api, headers=headers, json = body).json()

    results = [i["translations"][0]["text"] for i in response]+[i["name"] for i in img_resp]
    return results

def main(data):
    """
    drops invalid rows and returns the corrected df and error df
    """
    df = pd.DataFrame(data)
    df["name"] = df["name"].str.strip()
    
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

    
