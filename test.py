import requests
import pandas as pd

file4 = "https://lager.emilfolino.se/v2/products/everything"

response= requests.get(file4)
products_dict = response.json()["data"]

df = pd.DataFrame(products_dict)


# all the names
x = df.iloc[:, 2]

#dict with all unique names, stock set to 0
total_amount = {i: 0 for i in set(x)}


for naming, amo in zip(df.iloc[:, 2], df.iloc[:, 5]):
    if type(amo) is int and amo != 0:
        total_amount[naming] += amo

df = df.drop_duplicates(subset="name")
#print(df)

x = ["name", "stock", "total"]

k = ["Skruv M14", 3, 0]
p = ["Skruv M14", 3, 0]
L = ["Mutter M12", 2, 0]

D = []
#d = {i: 0 for i in x}

for i in [k,p,L]:
    d = {i: 0 for i in x}
    d["name"] =i[0]
    d["stock"] = i[1]
    d["total"] = i[2]
    D.append(d)
    
#print(D) 

"""
func = lambda v, m: v+m
print(D)
for i in D:
    print(i["stock"], i["total"])
    print(func(i["total"], i["stock"]))
    print("\n")
"""

#bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
#d= {map(lambda v: sum(v),bills.values())}
#g= dict(map(lambda v: (v[0],sum(v[1])),bills.items()))
# prints