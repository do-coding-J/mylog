# 이동 평균선
def calculate_moving_averages(df, short_window=10, long_window=20):
    df['ma_short'] = df['close'].rolling(window=short_window).mean()
    df['ma_long'] = df['close'].rolling(window=long_window).mean()
    df['ma_diff'] = df['ma_short'] - df['ma_long']
    return df

# MACD 계산
def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    # 단기 이동 평균 계산
    short_ema = df['close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    # 장기 이동 평균 계산
    long_ema = df['close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    # MACD 계산
    df['macd'] = short_ema - long_ema
    # MACD의 신호선(Signal line) 계산
    df['macd_signal'] = df['macd'].ewm(span=signal_window, min_periods=1, adjust=False).mean()
    
    return df

# RSI
def calculate_rsi(df, column="close", period=14):
    """
    RSI를 계산하는 함수입니다.
    
    :param df: 데이터프레임, 'close' 열을 포함해야 합니다.
    :param column: RSI 계산에 사용할 열 이름 (기본값은 'close')
    :param period: RSI를 계산할 기간 (기본값은 14일)
    :return: RSI가 계산된 데이터프레임을 반환합니다.
    """
    delta = df[column].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    df['rsi'] = rsi
    return df

