import pandas as pd

df = pd.read_csv("stock1.csv")
print(df.isnull().values.any())    # Shot way
# print(df.isnull().values.sum())   # To count errors
# print(df.isnull())  # TO view all
