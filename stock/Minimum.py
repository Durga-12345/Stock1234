import pandas as pd

df = pd.read_csv("stock1.csv")
list1 = list(df.mean())
print(df.mean())
print(min(list1))
