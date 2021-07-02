import pandas as pd

df = pd.read_csv("stock1.csv")
print(df.head())    # first 5
print(df.tail())    # last 5
print(df.to_string())   # Entire file
print(df)   # Normal
