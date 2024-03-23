
# 볼린저 밴드 계산
def calculate_bolinger_band(df, window=20, sigma=2):
    # 이동 평균 계산
    df['ma'] = df['close'].rolling(window=window).mean()
    # 표준 편차 계산
    df['standard_deviation'] = df['close'].rolling(window=window).std()
    # 상단 볼린저 계산
    df['upper_band'] = df['ma'] + (df['standard_deviation'] * sigma)
    # 하단 볼린저 계산
    df['lower_band'] = df['ma'] - (df['standard_deviation'] * sigma)
    
    return df

def signalize_bolinger_band(df):
    signals = []
    
    # 1. close 값이 upper band 보다 높으면 1
    if df['close'] > df['upper_band']:
        df['bolinger_signal'] = 1
    # 2. close 값이 lower band 보다 낮으면 -1
    elif df['close'] < df['lower_band']:
        df['bolinger_signal'] = -1
    # 3. 그 외는 0
    else:
        df['bolinger_signal'] = 0
            
    counter = 0
    latest_count = 0
    for i in range(len(df)):
        counter = counter + df['bolinger_signal']
        
        if counter > 2:
            if(latest_count < counter):
                df['bolinger_result'] = 'hold'
            else:
                df['bolinger_result'] = 'sell'
        
        elif counter < -2:
            
                