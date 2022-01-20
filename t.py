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

#df['stock'].replace('None' or str, 0, inplace=True)
#df = df.drop_duplicates(subset="name")

#bills = {"Alice": [20, 15, 30], "Bob": [10, 35]}
#d= {map(lambda v: sum(v),bills.values())}
#g= dict(map(lambda v: (v[0],sum(v[1])),bills.items()))
# prints
#print('d: ',dict(d))
#print('g: ',g)

#n = df.loc[df["name"] == "Skruv M14"]

#print(df)

        #temp_counter[naming] += amo
    #temp_counter[naming] += amo
    #print(naming, amo)
#print(temp_counter)
#print(df.iloc[:, 5])

"""
df = pd.DataFrame(products_dict["data"])
#df2 = df.iloc[0:40, :]
#print(df.iloc[0:100, :])
#print(df.loc[df["name"] == "Skruv M14"])
#print(df)
df = df.groupby(["id", "article_number", "name", "description", "specifiers", "stock", "location", "price"], as_index=False)["stock"].sum()
#df = df.groupby(list(df.keys()), as_index=False)["stock"].sum()
df = df.sort_values(by=["stock"])
df = df.drop_duplicates(subset="name", keep="last")
print("\n")
print(df.loc[df["name"] == "Skruv M14"])
#print(df.sort_values(by=["stock"]))

#df = df.drop_duplicates(subset="name")
#print(df.iloc[0])

#x = df.loc[df['column_name'] == some_value]
#products_dict = pd.DataFrame(products_dict)

# Prints first object of the data-list
#print(products_dict["data"][0])

# Prints name of first object of the data-list
#print(products_dict["data"][0]["name"])

"""