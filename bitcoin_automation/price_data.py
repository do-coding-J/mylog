import pyupbit
import datetime

def get_price(ticker, interval="minute1", count=200):
    return pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=count)

def get_price_past(ticker, interval="minute1", start_data=datetime.datetime(2024, 1, 1, 0, 0, 0), end_data=datetime.datetime(2024, 1, 2, 0, 0, 0)):
    return pyupbit.get_ohlcv_from(ticker=ticker, interval=interval, )