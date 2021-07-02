import pandas as pd

df = pd.read_csv("stock1.csv")
Sp500 = df["sp500"]
print(Sp500.mean())
