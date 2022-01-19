import requests
import pandas as pd

file4 = "https://lager.emilfolino.se/v2/products/everything"

response= requests.get(file4)
products_dict = response.json()

df = pd.DataFrame(products_dict["data"])

df = df.drop_duplicates(subset="name")
print(df.iloc[0])

#x = df.loc[df['column_name'] == some_value]
#products_dict = pd.DataFrame(products_dict)

# Prints first object of the data-list
#print(products_dict["data"][0])

# Prints name of first object of the data-list
#print(products_dict["data"][0]["name"])