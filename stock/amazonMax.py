import pandas as pd

df = pd.read_csv("stock1.csv")
print(df.iloc[df['AMZN'].idxmax()])
