import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock1.csv")
df.plot(x='Date')
plt.show()
