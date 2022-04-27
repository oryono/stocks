import csv
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')


def stock_price(symbol):
    url = 'https://finnhub.io/api/v1/quote?symbol=' + symbol + '&token=' + API_TOKEN
    req = requests.get(url)
    return req.json()


def generate_csv(stock):
    print(stock)
    (x, y) = stock

    headers = ['stock_symbol', 'percentage_change', 'current_price', 'last_close_price']
    data = [x, y['dp'], y['c'], y['pc']]

    with open('most_volatile_stock.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows([data])


if __name__ == '__main__':
    # Apple, Google, Amazon, Netflix, Facebook
    stocks = {}
    symbols = ['AAPL', 'GOOG', 'AMZN', 'NFLX', 'FB']
    for symbol in symbols:
        r = stock_price(symbol)
        stocks[symbol] = r

    s = sorted(stocks.items(), key=lambda x: x[1]['dp'])
    most_volatile_stock = s[0]

    #     Generate CSV
    generate_csv(most_volatile_stock)
