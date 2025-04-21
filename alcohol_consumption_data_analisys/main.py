import numpy as np
import pandas as pd

df=pd.read_csv('Alcohol_consumption.csv')
print('the whole data:')
print(df)
continents = df['WHO region'].max(5)

