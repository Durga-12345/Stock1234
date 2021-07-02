import pandas as pd
from sklearn import preprocessing as pre

df = pd.read_csv("stock1.csv")
va = df.values
scale = pre.MinMaxScaler()
a = scale.fit_transform(va)
normal = pd.DataFrame(a)
print(normal)
