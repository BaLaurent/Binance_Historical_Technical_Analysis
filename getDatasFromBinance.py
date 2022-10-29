from binance.client import Client
import json

client = Client()
nameOutputFile = input("Enter the name of the output file without extension :")
symbol = input("Enter the symbol (ex: BTCUSDT) : ")
interval = input("Enter the interval (ex: 1m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M) :")
startDate = input("Enter the start date (ex: 1 Jan, 2020) :")
endDate = input("Enter the end date (ex: 1 Jan, 2021) : ")
klines = client.get_historical_klines(symbol, interval, startDate, endDate)

# export the klines to a json file
with open(str(nameOutputFile)+'.json', 'w') as outfile:
    json.dump(klines, outfile)
    print("Json file created")

