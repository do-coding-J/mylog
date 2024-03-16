import pyupbit

# 회사
# access_key = 'stxke0a2rLTw8SaA14X1bPQoskS7eRsAPlrlHF8w'
# secret_key = 'wCUsmHh2ipIM2D3J2hM0huDAvidUrpqQDcBqZXra'
# 집
# access_key = 'stxke0a2rLTw8SaA14X1bPQoskS7eRsAPlrlHF8w'
# secret_key = 'wCUsmHh2ipIM2D3J2hM0huDAvidUrpqQDcBqZXra'

upbit = pyupbit.Upbit(access_key, secret_key)

target_ticker = "KRW-BTC"
target_interval = "minute1"

print(pyupbit.get_ohlcv(target_ticker, target_interval))

