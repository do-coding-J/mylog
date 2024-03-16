import csv
import pyupbit
from macd import get_macd
from ma import get_moving_average
from rsi import get_rsi
from macd import get_macd
from bolinger import get_bolinger

# 회사
# access_key = 'stxke0a2rLTw8SaA14X1bPQoskS7eRsAPlrlHF8w'
# secret_key = 'wCUsmHh2ipIM2D3J2hM0huDAvidUrpqQDcBqZXra'
# 집
access_key = 'ITNyUUhhogFWMbzL0BHQKcToJwfNfqlDDBBuXnvx'
secret_key = 'FboTePoLf7ULrwJwmIJx3vtHPD9xOPtRrxtxD492'

upbit = pyupbit.Upbit(access_key, secret_key)

# tickers = pyupbit.get_tickers()
# print(tickers)
# print(type(tickers))

# krw_tickers = pyupbit.get_tickers("KRW")
# print(krw_tickers)
# print(type(krw_tickers))

krw = "KRW"
btc = "BTC"

target_ticker = krw+"-"+btc

# minute1 = pyupbit.get_ohlcv(target_ticker, "minute1")
# print(minute1)
# print(type(minute1))

# minute10 = pyupbit.get_ohlcv(target_ticker, "minute10")
# print(minute10)
# print(type(minute10))

# minute60 = pyupbit.get_ohlcv(target_ticker, "minute60")
# print(minute60)
# print(type(minute60))

# day1 = pyupbit.get_ohlcv(target_ticker, "day")
# print(day1)
# print(type(day1))

# week1 = pyupbit.get_ohlcv(target_ticker, "week")
# print(week1)
# print(type(week1))

# month1 = pyupbit.get_ohlcv(target_ticker, "month")
# print(month1)
# print(type(month1))

target_interval = "minute1"



# 이평선 계산
test_ticker = target_ticker
test_interval = target_interval
test_window = 20
moving_avg = get_moving_average(target_ticker, test_interval, test_window)
# print(moving_avg)

# rsi 계산
test_interval = "minute10"
test_rsi_count = 14
test_rsi_signal_count = 9
rsi_val = get_rsi(test_ticker, test_interval, test_rsi_count)
rsi_sig = get_rsi(test_ticker, test_interval, test_rsi_signal_count)

# print(rsi_val, rsi_sig)

# macd 계산
test_interval_fast = 12
test_interval_slow = 26
test_interval_signal = 9

macd, macd_sig = get_macd(test_ticker, test_interval, test_interval_fast, test_interval_slow, test_interval_signal)
# print(macd)
# print(macd_sig)

# bolinger band
upper_band, sma, lower_band = get_bolinger(test_ticker)
print(upper_band)
print(lower_band)