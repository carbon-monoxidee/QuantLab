#Quantative Strategy Backtesting & Evaluation Engine 

from backtesting import Backtest, Strategy
from backtesting.test import GOOG #Google Stock data
import talib #calculate financial technical indicators
from backtesting.lib import crossover
import numpy as np, pandas as pd
import seaborn as sns, matplotlib.pyplot as plt

print(GOOG)

def optimizer_function(series):
    if series['# Trades']<10:
        return -1
    return series['Equity Final [$]']/series['Exposure Time [%]']

class RSI_Osicillator(Strategy):

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

bt=Backtest(GOOG,RSI_Osicillator,cash=10_000,commission=.01)
stats,heatmap=bt.optimize(
    upper_bound=range(50,85,5),
    lower_bound=range(10,45,5),
    rsi_window=range(10,30,2),
    maximize=optimizer_function,
    return_heatmap=True
)
#print(stats)
hm=heatmap.groupby(['upper_bound','lower_bound']).mean().unstack()
sns.heatmap(hm,annot=True,fmt='.2f',cmap='RdYlGn') # annote displays the value of each cell in the heatmap
plt.show()
lower_bound=stats['_strategy'].lower_bound
upper_bound=stats['_strategy'].upper_bound
strategy=stats['_strategy']
#bt.plot(filename=r'C:\Codes\temp\{strategy}-{lower_bound}-{upper_bound}.html',open_browser=True) 
