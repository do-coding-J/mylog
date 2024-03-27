import pyupbit
from transaction import *
from indicators import *
import logging

logging.basicConfig(filename='trading.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def should_buy(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=200)  # 최근 데이터 가져오기
    df = calculate_macd(df)
    df = calculate_rsi(df)
    df = calculate_moving_averages(df)

    latest_row = df.iloc[-1]  # 가장 최근 데이터
    
    # 매수 조건
    macd_cross_up = latest_row['macd'] > latest_row['macd_signal'] and latest_row['macd'] < 0
    rsi_low = latest_row['rsi'] < 35
    ma_diff_positive = latest_row['ma_diff'] > 0

    return macd_cross_up and rsi_low and ma_diff_positive

def trading_logic(ticker):
    balance_info = get_balance()  # 보유 잔고 조회
    current_price = pyupbit.get_current_price(ticker)  # 현재 가격 조회
    
    # KRW 잔고 추출
    krw_balance = next((item for item in balance_info if item['currency'] == 'KRW'), None)
    if krw_balance is not None:
        krw_balance = float(krw_balance['balance'])
    else:
        logging.info("KRW 잔고 조회 실패")
        return
    
    use_money = max(5000, round(krw_balance * 0.25, -3))  # 사용 금액 조정 및 최소 주문 금액 확인
    
    if should_buy(ticker):
        # 매수 로직
        buy_order_id = buy_money(ticker, current_price, use_money)
        logging.info(f"매수 주문: {buy_order_id}")
    else:
        logging.info("매수 조건 미충족")
    
    # 매도 조건 확인
    for coin in balance_info:
        if coin['currency'] == ticker.replace("KRW-", ""):
            holding_amount = float(coin['balance'])
            buy_price = float(coin['avg_buy_price'])
            profit_rate = (current_price - buy_price) / buy_price
            
            if profit_rate >= 0.1:
                # 익절 조건
                sell_order_id = sell(ticker, current_price, holding_amount * 0.5)  # 50% 매도
                logging.info(f"익절 매도 주문: {sell_order_id}")
            elif profit_rate <= -0.05:
                # 손절 조건
                sell_order_id = sell(ticker, current_price, holding_amount)  # 전량 매도
                logging.info(f"손절 매도 주문: {sell_order_id}")
            break
