import pyupbit
from transaction import *
from indicators import *
import logging

logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def should_buy(df):
    latest_row = df.iloc[-1]
    macd_cross_up = (latest_row["macd"] > latest_row["macd_signal"] and latest_row["macd"] < 0)
    rsi_low = latest_row["rsi"] < 35
    ma_diff_positive = latest_row["ma_diff"] > 0
    return macd_cross_up and rsi_low and ma_diff_positive

def should_sell(df, ticker, current_price, holding_amount, avg_buy_price):
    if holding_amount <= 0:
        return False

    profit_rate = (current_price - avg_buy_price) / avg_buy_price
    if profit_rate >= 0.3 or profit_rate <= -0.05:
        return True

    latest_row = df.iloc[-1]
    prev_row = df.iloc[-2]
    macd_cross_down = (latest_row["macd"] < latest_row["macd_signal"] and prev_row["macd"] > prev_row["macd_signal"])
    rsi_high = latest_row["rsi"] > 70
    return macd_cross_down or rsi_high

def trading_logic(ticker):
    # 데이터 불러오기 및 지표 계산
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=200)
    if df is None:
        logging.error("OHLCV 데이터 불러오기 실패")
        return
    
    df = calculate_macd(df)
    df = calculate_rsi(df)
    df = calculate_moving_averages(df)
    
    current_price = pyupbit.get_current_price(ticker)
    if current_price is None:
        logging.error("현재 가격 조회 실패")
        return

    # 보유한 코인의 정보 조회
    holding_amount, avg_buy_price = get_balance(ticker)
    
    # 매수 조건 검사
    if should_buy(df) and holding_amount <= 0:
        # KRW 잔고 조회 및 매수 금액 계산
        krw_balance = get_balance("KRW")
        use_money = max(
            5000, round(krw_balance * 0.25, -3)
        )  # 사용 금액 조정 및 최소 주문 금액 확인

        # 매수 주문
        buy_order_id = buy_money(ticker, current_price, use_money)
        if buy_order_id:
            logging.info(f"매수 주문: {buy_order_id}")
            # 주문 상태 확인 및 처리
            check_and_handle_order_status(buy_order_id, ticker)
        else:
            logging.info("매수 조건 미충족 또는 매수 주문 실패")

    # 매도 조건 검사
    if should_sell(df, ticker, current_price, holding_amount, avg_buy_price):
        # 해당 코인의 보유량 조회
        holding_amount, _ = get_balance(ticker=ticker)

        # 매도 주문
        sell_order_id = sell(ticker, current_price, holding_amount)
        if sell_order_id:
            logging.info(f"매도 주문: {sell_order_id}")
            # 주문 상태 확인 및 처리
            check_and_handle_order_status(sell_order_id, ticker)
        else:
            logging.info("매도 조건 미충족 또는 매도 주문 실패")
