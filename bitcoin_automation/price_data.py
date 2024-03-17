import pyupbit

def get_price(ticker, interval, count=200):
    return pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=count)

# def get_price_past(ticker, interval, start_data, end_data):
#     return pyupbit.get_ohlcv_from(ticker=ticker, interval=interval, )