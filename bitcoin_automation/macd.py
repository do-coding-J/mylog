from price_data import get_price

def get_macd(ticker, interval, day_fast, day_slow, day_sig):
    price_data = get_price(ticker=ticker, interval=interval, count=100)
    
    emafast = price_data['close'].ewm(span=day_fast,min_periods=0, adjust=False).mean()
    emaslow = price_data['close'].ewm(span=day_slow,min_periods=0, adjust=False).mean()
    
    macd = emafast - emaslow
    
    sig_line = macd.ewm(span=day_sig,min_periods=0, adjust=False).mean()
    
    return macd, sig_line