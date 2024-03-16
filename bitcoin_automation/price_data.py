import pyupbit

def get_price(ticker, interval, count=200):
    return pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=count)