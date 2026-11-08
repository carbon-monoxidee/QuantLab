#Quantative Strategy Backtesting & Evaluation Engine 

from backtesting import Backtest, Strategy
from backtesting.test import GOOG #Google Stock data
import talib #calculate financial technical indicators
from backtesting.lib import crossover
import numpy as np, pandas as pd

print(GOOG)

def optimizer_function(series):
    if series['# Trades']<10:
        return -1
    return series['Equity Final [$]']/series['Exposure Time [%]']

class STRATEGY(Strategy):

    upper_bound=70
    lower_bound=30
    rsi_window=14
    def init(self):
        self.rsi=self.I(talib.RSI,self.data.Close, self.rsi_window)
    def next(self):
        if crossover(self.rsi,self.upper_bound) :
            self.position.close()
        elif crossover(self.lower_bound,self.rsi):
            self.buy()

bt=Backtest(GOOG,STRATEGY,cash=10_000,commission=.01)
stats=bt.optimize(
    upper_bound=range(50,85,5),
    lower_bound=range(10,45,5),
    rsi_window=range(10,30,2),
    maximize=optimizer_function
)
print(stats)
bt.plot(filename=r'C:\Codes\temp\backtesting.html',open_browser=True) 
