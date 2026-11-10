import ccxt , pandas as pd, numpy as np
from datetime import datetime, timedelta

ex=ccxt.binance({"enableRateLimit":True})
print(ex.fetch_ticker('BTC/USDT'))