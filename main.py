import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stock_list = ["AAPL", "MSFT", "TSLA", "SPY", "META", "NFLX", "PFE", "IBM", "EA", "PZZA",
               "HL", "INTC", "AMZN", "NVDA", "VOD", "DJI", "TSCO", "BAC", "JPM", "DIS"]
stocks = yf.download(stock_list, start="2015-01-01", end="2021-01-01")

close = stocks.loc[:,"Close"].copy()

normclose = close.div(close.iloc[0]).mul(100)

normclose.plot(figsize=(25,15),fontsize=12)
plt.legend(fontsize=20)
# plt.show()

returns = close.pct_change().dropna()

summary = returns.describe().T.loc[:,["mean","std"]]

summary["mean"] = summary["mean"]*252
summary["std"] = summary["std"]*np.sqrt(252)

summary.plot.scatter(x="std",y="mean",figsize=(12,8),s=50,fontsize=15)
for i in summary.index:
    plt.annotate(i,xy=(summary.loc[i,"std"]+0.002,summary.loc[i,"mean"]+0.002),size=15)
plt.xlabel("Annual risk(std)",fontsize = 15)
plt.ylabel("Annual return",fontsize = 15)
plt.title("Risk/return",fontsize=25)
# plt.show()

plt.figure(figsize=[15,10])
sns.set(font_scale=1.5) 
sns.heatmap(returns.corr(),cmap="Reds" ,annot=True, annot_kws={"size":15},vmax=0.7)
plt.show()

