#Quantative Strategy Backtesting & Evaluation Engine 

from backtesting import Backtest, Strategy
from backtesting.test import GOOG #Google Stock data
import talib #calculate financial technical indicators
from backtesting.lib import crossover
import numpy as np, pandas as pd

print(GOOG)

class STRATEGY(Strategy):

    upper_bound=80
    lower_bound=20
    def init(self):
        self.rsi=self.I(talib.RSI,self.data.Close)
    def next(self):
        if crossover(self.rsi,self.upper_bound) :
            self.position.close()
        elif crossover(self.lower_bound,self.rsi):
            self.buy()

bt=Backtest(GOOG,STRATEGY,cash=1000,commission=.01)
stats=bt.run()
print(stats)