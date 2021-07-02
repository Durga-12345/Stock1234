import pandas as pd

df = pd.read_csv("stock1.csv")
for i in df.columns:
    if i == "Date":
        continue
    print(i)
# print(sorted(df))
# print(list(df.columns))
# print(list(df.columns.values))
# print(list(df.columns.values.tolist()))
