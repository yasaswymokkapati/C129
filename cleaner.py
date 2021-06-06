import pandas as pd
import csv

df = pd.read_csv("final 4.csv")
print(df.shape)

del df['Star_name']
del df['Radius']
del df['Distance']
del df['Mass']
del df['Luminosity']

print(df.shape)