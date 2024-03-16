from price_data import get_price

def get_bolinger(ticker, interval='minute', count=20, num_std_dev=12):
    price_data = get_price(ticker=ticker, interval=interval, count=count)
    
    sma = price_data['close'].rolling(window=count).mean()
    
    upper_band = sma + num_std_dev * price_data['close'].rolling(window=count).std()
    lower_band = sma - num_std_dev * price_data['close'].rolling(window=count).std()
    
    return upper_band.iloc[-1], sma, lower_band.iloc[-1]
    