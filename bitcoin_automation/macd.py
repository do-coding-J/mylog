
# MACD 계산
def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    # 단기 이동 평균 계산
    short_ema = df['close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    # 장기 이동 평균 계산
    long_ema = df['close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    # MACD 계산
    df['macd_val'] = short_ema - long_ema
    # MACD의 신호선(Signal line) 계산
    df['macd_signal'] = df['macd_val'].ewm(span=signal_window, min_periods=1, adjust=False).mean()
    
    return df



'''
macd의 조건은 
1. macd와 sig가 모두 음수 일 때 macd가 sig를 넘어 설 때 buy
2. macd와 sig가 모두 양수일 때 macd sig diff가 -30000 이상이면 sell 
'''

def signalize_macd(df):
    signals = []
    position = None
    for i in range(len(df)):
        # 조건 1: MACD와 Signal이 모두 음수이고 MACD가 Signal을 넘어설 때 Buy 신호 생성
        if df['macd_val'].iloc[i] < 0 and df['macd_signal'].iloc[i] < 0 and df['macd_val'].iloc[i] > df['macd_signal'].iloc[i]:
            signals.append('Buy')
            position = 'long'
        # 조건 2: MACD와 Signal이 모두 양수이고 MACD - Signal이 -30000 이상일 때 Sell 신호 생성
        elif df['macd_val'].iloc[i] > 0 and df['macd_signal'].iloc[i] > 0 and (df['macd_val'].iloc[i] - df['macd_signal'].iloc[i]) <= -30000:
            signals.append('Sell')
            position = None
        else:
            signals.append('Hold')
    df['macd_result'] = signals
    return df