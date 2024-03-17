import pyupbit

# 회사
# access_key = 'stxke0a2rLTw8SaA14X1bPQoskS7eRsAPlrlHF8w'
# secret_key = 'wCUsmHh2ipIM2D3J2hM0huDAvidUrpqQDcBqZXra'
# 집
access_key = "ITNyUUhhogFWMbzL0BHQKcToJwfNfqlDDBBuXnvx"
secret_key = "FboTePoLf7ULrwJwmIJx3vtHPD9xOPtRrxtxD492"

upbit = pyupbit.Upbit(access_key, secret_key)

# ask price = 매도 호가 (팔고 싶어하는 가격) = 내가 살 가격
# bid price = 매수 호가 (사고 싶어하는 가격) = 내가 팔 가격
def buy_amount(ticker, price, amount):
    try:
        orderbook = pyupbit.get_orderbook(ticker=ticker)
        sell_price = orderbook["orderbook_units"][0]["ask_price"]
        if price >= sell_price:
            upbit.buy_limit_order(ticker=ticker, price=price, volume=amount)
            print(f"{ticker} {price}원에 {amount}개 매수 주문 완료")
        else:
            print(
                f"{ticker}의 현재 가격이 지정한 가격보다 낮아 매수 주문을 실행할 수 없습니다."
            )
    except Exception as e:
        price("매수 주문 에러 : ", e)
        
def buy_money(ticker, price, money):
    try:
        orderbook = pyupbit.get_orderbook(ticker=ticker)
        sell_price = orderbook["orderbook_units"][0]["ask_price"]
        amount = money / sell_price
        if price >= sell_price:
            order_id = upbit.buy_limit_order(ticker=ticker, price=price, volume=amount)
            print(f"{ticker} {price}원에 {amount}개 매수 주문 완료 id : {order_id}")
            return order_id
        else:
            print(
                f"{ticker}의 현재 가격이 지정한 가격보다 낮아 매수 주문을 실행할 수 없습니다."
            )
    except Exception as e:
        price("매수 주문 에러 : ", e)


def sell(ticker, price, amount):
    try:
        orderbook = pyupbit.get_orderbook(ticker=ticker)
        buy_price = orderbook["orderbook_units"][0]["bid_price"]
        if price <= buy_price:
            order_id = upbit.sell_limit_order(ticker=ticker, price=price, volume=amount)
            print(f"{ticker} {price}원에 {amount}개 매도 주문 완료 id : {order_id}")
            return order_id
        else:
            print(
                f"{ticker}의 현재 가격이 지정한 가격보다 높아 매도 주문을 실행할 수 없습니다."
            )
    except Exception as e:
        print("매도 주문 에러:", e)
        
def get_balance():
    try:
        balance = upbit.get_balances()
        for coin in balance:
            if coin['currency'] == 'KRW':
                print(f"보유 현금: {coin['balance']}")
            else:
                print(f"보유 코인: {coin['currency']}, 잔고: {coin['balance']}")
    except Exception as e:
        print("잔고 조회 에러:", e)