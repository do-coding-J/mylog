import pyupbit
from macd import *
from ma import *
from price_data import *
from rsi import *
from bolinger import *
from transaction import *
import matplotlib.pyplot as plt

plt.ion()  # 대화형 모드 활성화

krw = "KRW"
btc = "BTC"

target_ticker = krw + "-" + btc

"""
매매 전략 
지표 순위 :

볼린저 밴드는 DAY로만 측정 하기

매수 : 
    1. 볼린저 밴드가 연속으로 2번 이상 lower_band보다 떨어지는 경우
    2. MACD에서 신호선보다 일정 비율로 높아질 경우
    3. RSI에서 신호선 보다 위에 있는 경우
    4. 이평선 20이 이평선 60보다 높아질 경우
    5. 이평선 60이 이평선 120보다 높아질 경우
    6. 수익이 -10% 이하 일 경우

매도 :
    1. 수익이 5%이상 났을 경우
    2. 수익이 -20%이하로 떨어졌을 경우 -> 알림
    3. 볼린저 밴드가 연속으로 2번 이상 upper_band보다 높아지는 경우
    4. MACD에서 신호선보다 일정 비율로 낮아질 경우
    5. RSI에서 신호선 보다 밑에 있는 경우
    6. 이평선 20이 이평선 60보다 낮아질 경우
    7. 이평선 60이 이평선 120보다 낮아질 경우
"""

# 백테스트 방법
# print(pyupbit.get_ohlcv_from(ticker=target_ticker, interval="minute10", fromDatetime=datetime.datetime(2024, 1, 1, 0, 0, 0), to=datetime.datetime(2024, 3, 1, 0, 0, 0)))

while True:
    df = pyupbit.get_ohlcv(ticker=target_ticker, interval="minute1", count=200)
    macd_df = signalize_macd(calculate_macd(df=df))