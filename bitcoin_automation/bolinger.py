from price_data import get_price
import pandas as pd
import matplotlib.pyplot as plt

def get_bolinger(ticker, interval='day', count=200, window=20, num_std_dev=2):
    price_data = get_price(ticker=ticker, interval=interval, count=count)
    
    sma = price_data['close'].rolling(window=window).mean()
    
    upper_band = sma + num_std_dev * price_data['close'].rolling(window=window).std()
    lower_band = sma - num_std_dev * price_data['close'].rolling(window=window).std()
    
    bolinger_df = pd.DataFrame({
        'open' : price_data['open'],
        'high' : price_data['high'],
        'low' : price_data['low'],
        'close' : price_data['close'],
        'volume' : price_data['volume'],
        'value' : price_data['value'],
        'Upper' : upper_band,
        'SMA' : sma,
        "Lower" : lower_band
    })
    
    return bolinger_df

def plot_bolinger_band(bolinger_df):
    plt.figure(figsize=(14, 7))
    
    # 이동평균선 그래프
    plt.plot(bolinger_df.index, bolinger_df['close'], label='close', color='blue')
    
    # 볼린저 밴드 그래프
    plt.plot(bolinger_df.index, bolinger_df['Upper'], label='Upper Band', color='red', linestyle='--')
    plt.plot(bolinger_df.index, bolinger_df['Lower'], label='Lower Band', color='green', linestyle='--')
    
    # 그래프 제목과 축 라벨 설정
    plt.title('Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    
    # 범례 추가
    plt.legend()
    
    # 그래프 출력
    plt.show()
    
    
def check_bolinger_signal(ticker, interval="day"):
    # 1분 기준 떨어지면 -1 올라가면 1 그 외는 0
    ret_df = get_bolinger(ticker=ticker, interval=interval)
    
    # 현재가격이 lower band보다 낮으면서 upper band보다 높은 경우 'Hold'로 표시
    ret_df['Signal'] = 'Hold'
    ret_df.loc[(ret_df['close'] < ret_df['Lower']) & (ret_df['close'] > ret_df['Upper']), 'Signal'] = 'Hold'
    
    # 현재가격이 lower band보다 낮은 경우 'Buy'로 표시
    ret_df.loc[ret_df['close'] < ret_df['Lower'], 'Signal'] = 'Buy'
    
    # 현재가격이 upper band보다 높은 경우 'Sell'로 표시
    ret_df.loc[ret_df['close'] > ret_df['Upper'], 'Signal'] = 'Sell'
    
    # 가장 최근 데이터부터 검사
    signal_series = ret_df['Signal'].iloc[::-1]
    
    consecutive_buy = 0
    consecutive_sell = 0
    
    # 연속된 buy와 sell 신호를 검사하여 조건에 따라 반환값을 결정
    for signal in signal_series:
        if signal == 'Buy':
            consecutive_buy += 1
            consecutive_sell = 0
        elif signal == 'Sell':
            consecutive_sell += 1
            consecutive_buy = 0
        else:
            consecutive_buy = 0
            consecutive_sell = 0
            
        if consecutive_buy >= 2:
            return 1
        elif consecutive_sell >= 2:
            return -1
    
    # 위 조건을 만족하지 않으면 0을 반환
    return 0