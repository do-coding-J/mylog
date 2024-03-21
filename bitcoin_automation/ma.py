from price_data import get_price

def get_moving_average(ticker, interval="minute", window=20):
    price_data = get_price(ticker=ticker, interval=interval)
    return price_data['close'].rolling(window=window).mean()
    