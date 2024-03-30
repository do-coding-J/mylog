import json
import pyupbit
import time
import logging

logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

with open("key.json", "r") as f:
    key = json.load(f)

access_key = key["access_key"]
secret_key = key["secret_key"]
upbit = pyupbit.Upbit(access_key, secret_key)


# ask price = 매도 호가 (팔고 싶어하는 가격) = 내가 살 가격
# bid price = 매수 호가 (사고 싶어하는 가격) = 내가 팔 가격
def buy_amount(ticker, price, amount):
    try:
        orderbook = pyupbit.get_orderbook(ticker=ticker)
        sell_price = orderbook["orderbook_units"][0]["ask_price"]
        if price >= sell_price:
            upbit.buy_limit_order(ticker=ticker, price=price, volume=amount)
            logging.info(f"{ticker} {price}원에 {amount}개 매수 주문 완료")
        else:
            logging.info(
                f"{ticker}의 현재 가격이 지정한 가격보다 낮아 매수 주문을 실행할 수 없습니다."
            )
    except Exception as e:
        logging.error(f"예상치 못한 오류 발생: {e}", exc_info=True)


def buy_money(ticker, price, money):
    try:
        orderbook = pyupbit.get_orderbook(ticker=ticker)
        sell_price = orderbook["orderbook_units"][0]["ask_price"]
        amount = money / sell_price
        if price >= sell_price:
            order_id = upbit.buy_limit_order(ticker=ticker, price=price, volume=amount)
            logging.info(
                f"{ticker} {price}원에 {amount}개 매수 주문 완료 id : {order_id}"
            )
            return order_id
        else:
            logging.info(
                f"{ticker}의 현재 가격이 지정한 가격보다 낮아 매수 주문을 실행할 수 없습니다."
            )
    except Exception as e:
        logging.error(f"매수 주문 중 예상치 못한 오류 발생: {e}", exc_info=True)
        logging.info(
                f"{ticker} {price}원에 {amount}개 매수 주문 시도 id : {order_id}"
            )


def sell(ticker, price, amount):
    try:
        orderbook = pyupbit.get_orderbook(ticker=ticker)
        buy_price = orderbook["orderbook_units"][0]["bid_price"]
        if price <= buy_price:
            order_id = upbit.sell_limit_order(ticker=ticker, price=price, volume=amount)
            logging.info(
                f"{ticker} {price}원에 {amount}개 매도 주문 완료 id : {order_id}"
            )
            return order_id
        else:
            logging.info(
                f"{ticker}의 현재 가격이 지정한 가격보다 높아 매도 주문을 실행할 수 없습니다."
            )
    except Exception as e:
        logging.error(f"매도 주문 중 예상치 못한 오류 발생: {e}", exc_info=True)
        logging.info(
                f"{ticker} {price}원에 {amount}개 매도 주문 시도 id : {order_id}"
            )

def get_balance(ticker):
    """
    특정 코인에 대한 보유량과 매수 평균 가격을 조회합니다.

    :param ticker: 조회할 코인의 티커 (예: "KRW-BTC")
    :return: 보유량과 매수 평균 가격
    """
    try:
        balances = upbit.get_balances()
        for balance in balances:
            if balance["currency"] == ticker.replace("KRW-", ""):
                avg_buy_price = float(balance["avg_buy_price"])  # 매수 평균 가격
                holding_amount = float(balance["balance"])  # 보유량
                return holding_amount, avg_buy_price
    except Exception as e:
        logging.error(f"잔고 조회 중 예상치 못한 오류 발생: {e}", exc_info=True)
        logging.info(f"{balances}")
        return 0, 0
    return 0, 0  # 해당 코인을 보유하지 않는 경우


def cancel_order(order_id):
    try:
        result = upbit.cancel_order(order_id)
        logging.info(f"주문 취소 성공: {order_id}")
        return result
    except Exception as e:
        logging.error(f"주문 취소 실패: {order_id}, 에러: {e}", exc_info=True)


def check_and_handle_order_status(order_id, ticker, wait_time=60, check_interval=10):
    """
    주문 상태를 주기적으로 확인하고, 필요에 따라 주문을 취소하거나 추가 조치를 취합니다.

    :param order_id: 확인할 주문의 ID
    :param ticker: 주문한 티커
    :param wait_time: 주문 체결을 기다리는 최대 시간(초)
    :param check_interval: 주문 상태 확인 간격(초)
    """
    start_time = time.time()
    while time.time() - start_time < wait_time:
        # 주문 상태 확인
        order_detail = upbit.get_order(order_id)
        if order_detail["state"] == "done":
            logging.info(f"주문 {order_id} 체결 완료")
            return True
        elif order_detail["state"] == "cancel":
            logging.info(f"주문 {order_id} 이미 취소됨")
            return False

        # 주문 상태를 일정 간격으로 확인
        time.sleep(check_interval)

    # 주문이 wait_time 동안 체결되지 않은 경우, 주문 취소 시도
    cancel_result = cancel_order(order_id)
    if cancel_result:
        logging.info(f"주문 {order_id} 체결 대기 시간 초과, 주문 취소 시도 성공")
    else:
        logging.error(
            f"주문 {order_id} 체결 대기 시간 초과, 주문 취소 시도 실패", exc_info=True
        )
        

    return False
