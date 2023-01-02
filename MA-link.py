import datetime as date
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import pandas_datareader.data as web
import matplotlib.pyplot as plt


df = web.DataReader('BTC-USD', 'yahoo', start='2020-09-1', end='2022-12-06')
df.head(20)

plt.figure(figsize=(13,6))
df.Close.plot()

#creamos una nueva figura su tamaño width, height en inches
MA=pd.Series(pd.Series.rolling(df['Close'],100).mean(),name='MA_'+str(100))
df=df.join(MA)


Data=df[['Close','MA_50','MA_100']]


Data.plot(figsize=(16,8))