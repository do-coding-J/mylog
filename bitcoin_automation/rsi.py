from price_data import *

def get_rsi(ticker, interval, count=14):
    price_data = get_price(ticker=ticker, interval=interval, count=count+1)
    price_diff = price_data['close'].diff()
    
    up, down = price_diff.copy(), price_diff.copy()
    up[up<0] = 0
    down[down>0] = 0
    
    up_avg = up.rolling(count).mean()
    down_avg = abs(down.rolling(count).mean())
    
    rs = up_avg / down_avg
    rsi = 100 - (100 / (1+rs))
    
    return rsi.iloc[-1]