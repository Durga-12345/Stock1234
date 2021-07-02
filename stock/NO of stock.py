import pandas as pd

df = pd.read_csv("stock1.csv")
# print(df.info())    # All info
# print(len(df))  # rows
print(len(df.columns)-2)  # columns
