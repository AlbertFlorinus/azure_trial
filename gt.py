x = 12
k = ["hej"]
y = {i:[10000000000000000000,2] for i in k}

import pandas as pd
df = pd.DataFrame(y)
#print(df)

g = df.loc[df["hej"]==10000000000000000000]

#print(type(10000000000000000000))