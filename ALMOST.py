import requests
import pandas as pd
import sys
import numpy as np

file4 = "https://lager.emilfolino.se/v2/products/everything"

response= requests.get(file4)
products_dict = response.json()["data"]

data = products_dict

df = pd.DataFrame(products_dict)

total_amount = {i: 0 for i in set(df["name"])}

error_col = []

for i in data:
    naming = i["name"]
    try:
        total_amount[naming] += i["stock"]

    except:

        error_col.append(i)

df = df.drop_duplicates(subset="name")

for i in total_amount.keys():
    df.loc[df["name"] == i, "total"] = total_amount[i]

#for i in error_col:
    #print(i["stock"], i["name"])