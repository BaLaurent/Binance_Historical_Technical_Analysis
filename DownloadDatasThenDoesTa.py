import talib as ta
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from binance.client import Client

client = Client()
symbol = input("Enter the symbol (ex: BTCUSDT) : ")
interval = input("Enter the interval (ex: 1m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M) :")
startDate = input("Enter the start date (ex: 1 Jan, 2020) :")
endDate = input("Enter the end date (ex: 1 Jan, 2021) : ")
klines = client.get_historical_klines(symbol, interval, startDate, endDate)

outputFile = input("Enter the relative path of the output file with the filename and extension (ex: datas/output.csv) :")

# Create a dataframe
df = pd.DataFrame(klines, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])

# get Indicators
df['RSI'] = ta.RSI(df['Close'], timeperiod=30)
macd, macdsignal, macdhist = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
df["MACD"] = macd
df["MACDSignal"] = macdsignal
df["MOM"] = ta.MOM(df["Close"], timeperiod=10)
fastk, fastd = ta.STOCHRSI(df["Close"], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
df["Stoch.RSI.K"] = fastk
df["Stoch.RSI.D"] = fastd
df["CCI20"] = ta.CCI(df["High"], df["Low"], df["Close"], timeperiod=20)
df["ADX"] = ta.ADX(df["High"], df["Low"], df["Close"], timeperiod=14)
df["ADX+DI"] = ta.PLUS_DI(df["High"], df["Low"], df["Close"], timeperiod=14)
df["ADX-DI"] = ta.MINUS_DI(df["High"], df["Low"], df["Close"], timeperiod=14)
df["AO"] = ta.AROONOSC(df["High"], df["Low"], timeperiod=14)
df["W.R"] = ta.WILLR(df["High"], df["Low"], df["Close"], timeperiod=14)
bbUpper, bbMiddle, bbLower = ta.BBANDS(df["Close"], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
df["BBUpper"] = bbUpper
df["BBMiddle"] = bbMiddle
df["BBLower"] = bbLower
df["UO"] = ta.ULTOSC(df["High"], df["Low"], df["Close"], timeperiod1=7, timeperiod2=14, timeperiod3=28)
df["EMA5"] = ta.EMA(df["Close"], timeperiod=5)
df["EMA10"] = ta.EMA(df["Close"], timeperiod=10)
df["EMA20"] = ta.EMA(df["Close"], timeperiod=20)
df["EMA30"] = ta.EMA(df["Close"], timeperiod=30)
df["EMA50"] = ta.EMA(df["Close"], timeperiod=50)
df["EMA100"] = ta.EMA(df["Close"], timeperiod=100)
df["EMA200"] = ta.EMA(df["Close"], timeperiod=200)
df["SMA5"] = ta.SMA(df["Close"], timeperiod=5)
df["SMA10"] = ta.SMA(df["Close"], timeperiod=10)
df["SMA20"] = ta.SMA(df["Close"], timeperiod=20)
df["SMA30"] = ta.SMA(df["Close"], timeperiod=30)
df["SMA50"] = ta.SMA(df["Close"], timeperiod=50)
df["SMA100"] = ta.SMA(df["Close"], timeperiod=100)
df["SMA200"] = ta.SMA(df["Close"], timeperiod=200)

# export df to csv file
df.to_csv(outputFile, index=False)
print("Finished")
