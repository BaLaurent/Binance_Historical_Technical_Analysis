from binance.client import Client
import json

api_key = '{YOUR_API_KEY}'
api_secret = '{YOUR_API_SECRET}'
client = Client(api_key, api_secret)
symbol = '{SYMBOL}' # example: 'BNBUSDT'
print("downloading data from Binance for symbol: " + symbol)
klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE,"30 Dec, 2017", "1 Jan, 2020")

# export the klines to a json file
with open('dataBinance_2018-2019_5m_unformated.json', 'w') as outfile:
    json.dump(klines, outfile)

