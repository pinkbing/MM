"""
Polling is a technique used to build real-time application where the client repeatedly sends requests to the server
to act on latest data. This is often done in a loop, where the program repeatedly checks for changes or updates.

Make a REST call every 2 seconds to Binance future exchange to print order book of BTCUSDT.

"""

import requests
import time
import logging
import numpy as np
from collections import deque



logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)

# Base endpoint
URL = 'https://fapi.binance.com'

# https://binance-docs.github.io/apidocs/futures/en/#order-book
METHOD = '/fapi/v1/depth'


def get_order_book(symbol):
    # GET request
    response = requests.get(URL + METHOD, params={'symbol': symbol})

    # convert to JSON object by response.json()
    order_book = response.json()

    # print best bid and offer price
    best_bid = float(order_book['bids'][0][0])
    best_ask = float(order_book['asks'][0][0])

    return [best_bid, best_ask]

# def historical_price
def calculate_midprice(bid, ask):
    return (ask + bid)/2


# use a while loop to query Binance once every 2 seconds
while True:
    # get best bid and offer
    prices = get_order_book("BTCUSDT")
    midprice = calculate_midprice(prices[0], prices[1])

    #logging.info('Best bid:{}, ask: {}'.format(prices[0], prices[1]))
    # Log results
    logging.info(f'Bid: {prices[0]:.2f}, Ask: {prices[1]:.2f}, Mid_Price: {midprice:.4f}')

    # sleep
    time.sleep(2)
