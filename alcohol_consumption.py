import numpy as np
import pandas as pd

df=pd.read_csv('Alcohol_consumption.csv')
print('the whole data:')
print(df)
continents = df['WHO region']
#right now I want to write a descriptive statistics of the alcohol consumption in different regions
