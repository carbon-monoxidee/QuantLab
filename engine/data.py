import ccxt , pandas as pd, numpy as np
from datetime import datetime, timedelta

ex=ccxt.binance({"enableRateLimit":True})
#print(ex.fetch_ticker('BTC/USDT'))

raw=ex.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=1000)#open, high, low, close, volume
#print(raw)
df=pd.DataFrame(raw, columns=['timestamp','open','high','low','close','volume'])

df['timestamp']=pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True) #inplace modifies the original dataframe instead of creating a new one
print(df.head())