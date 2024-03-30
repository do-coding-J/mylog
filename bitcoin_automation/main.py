import time
import logging
import datetime
from transaction import *
from indicators import *
from logic import *

logging.basicConfig(
    filename="trading.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def trading_bot():
    ticker = "KRW-BTC"
    while True:
        try:
            # 여기서는 ticker만 전달합니다.
            trading_logic(ticker)
        except Exception as e:
            # 오류 발생 시 logging을 사용합니다.
            logging.error(f"트레이딩 봇 실행 중 오류 발생: {e}")

        # 1분마다 반복. 전략에 따라 조정 가능합니다.
        time.sleep(60)

def simulate_trading(should_buy, should_sell, ticker, start_date, end_date, interval='day'):
    cash = 1000000  # 초기 자본금
    holding = 0  # 보유량
    avg_buy_price = 0  # 평균 매수 가격
    trade_log = []  # 거래 기록

    current_date = start_date
    while current_date <= end_date:
        print(current_date)
        # 데이터 불러오기
        df = pyupbit.get_ohlcv(ticker, interval=interval, to=current_date.strftime('%Y-%m-%d'))
        if df is None or df.empty:
            print("데이터를 불러오는 데 실패했습니다.")
            break
        df = calculate_macd(df)
        df = calculate_rsi(df)
        df = calculate_moving_averages(df)
        current_price = df.iloc[-1]['close']
        
        if should_buy(df) and cash > 0:
            # 매수
            holding = cash / current_price
            cash = 0
            avg_buy_price = current_price
            trade_log.append({'date': current_date, 'action': 'BUY', 'price': current_price})
        
            logging.info(f"buy")
        elif should_sell(df, ticker, current_price, holding, avg_buy_price) and holding > 0:  # 수정된 부분
            # 매도
            cash = holding * current_price
            holding = 0
            avg_buy_price = 0  # 매도 후 평균 매수 가격 리셋
            trade_log.append({'date': current_date, 'action': 'SELL', 'price': current_price})
            logging.info(f"sell")
        else :
            logging.info(f"hold")
        
        logging.info(f"date {current_date}, cash : {cash}, holding : {holding}, current price : {current_price}")
        # 다음 날짜로 이동
        current_date += datetime.timedelta(days=1)

    final_value = cash + (holding * current_price if holding > 0 else 0)  # 최종 자산 가치
    return final_value, trade_log

# 시뮬레이션 실행
ticker = "KRW-BTC"

final_value, trade_log = simulate_trading(should_buy, should_sell, ticker, datetime.datetime(2024,1,1,0,0,0), datetime.datetime(2024,3,30,0,0,0))

print(f"최종 자산 가치: {final_value}")
for log in trade_log:
    print(log)
    
"""
보충 내용
`logic.py`, `indicators.py`, 그리고 `transaction.py` 파일을 통해 구성한 알고리즘 트레이딩 시스템에는 몇 가지 보충해야 할 부분이 있습니다. 이러한 부분들을 보완하면 시스템의 효율성과 안정성을 높일 수 있습니다.

### 1. 에러 핸들링 강화:

- 현재 코드에서는 예외가 발생할 경우 간단히 출력만 하고 있습니다. 예외 처리를 통해 특정 에러 상황에서의 로직을 더 세밀하게 제어할 수 있도록 개선할 필요가 있습니다. 예를 들어, API 요청 제한에 도달했을 때 일정 시간 대기하는 로직을 추가할 수 있습니다.

### 2. 로깅 시스템 구축:

- 트레이딩 로봇의 운영 상황을 실시간으로 모니터링하고, 추후 분석이 가능하도록 로깅 시스템을 구축하는 것이 중요합니다. Python의 `logging` 모듈을 활용해 로그를 파일로 저장하도록 설정할 수 있습니다.

### 3. 설정 파일 활용:

- API 키와 같은 민감한 정보는 코드 내에 직접 적지 않는 것이 좋습니다. 이러한 정보는 환경 변수나 외부 설정 파일(`.env` 파일 등)에 저장하고, 코드에서는 이를 불러와 사용하는 방식을 추천합니다.

### 4. 백테스팅 기능:

- 알고리즘의 성능을 평가하기 위해 과거 데이터에 대한 백테스팅 기능을 구현하는 것이 필요합니다. 이를 통해 실제 투자 전에 전략의 유효성을 검증할 수 있습니다.

### 5. 주문 실행 조건의 세부 조정:

- `should_buy` 함수에서는 매수 조건을 결정합니다. 하지만 현재의 구현은 매우 기본적이며, 시장 상황이나 개별 암호화폐의 특성에 따라 다양한 조건을 추가하거나 조정할 필요가 있습니다.

### 6. 주문량 및 자금 관리 전략:

- 트레이딩 알고리즘에서는 자금 관리가 중요합니다. `buy_money` 함수에서는 매수할 금액을 결정하지만, 이는 전체 자금의 일정 비율을 기준으로 단순 계산됩니다. 시장 상황, 손실 한도, 다양성 유지 등을 고려한 보다 복잡한 자금 관리 전략이 필요합니다.

### 7. 실시간 데이터 처리:

- 암호화폐 시장은 매우 변동성이 크므로, 최신 시장 데이터를 실시간으로 처리하고 분석할 수 있는 기능이 중요합니다. 이를 위해 WebSocket과 같은 실시간 데이터 스트리밍 기술을 활용할 수 있습니다.

위 사항들을 고려하여 시스템을 개선하면, 보다 안정적이고 신뢰할 수 있는 알고리즘 트레이딩 시스템을 구축할 수 있을 것입니다.

추가 
보안: API 키의 안전한 관리
오류 처리: try-except 블록을 통한 오류 처리의 강화
함수 통합: 매매 로직과 실시간 데이터 처리의 연동
실시간 데이터 처리: while 루프 내에서 시장 데이터를 실시간으로 처리하는 로직
성능 최적화: API 호출 및 데이터 처리의 효율성
사용자 인터페이스(UI): 사용자가 쉽게 매매 전략을 설정하고 모니터링할 수 있는 인터페이스 제공
백테스팅 및 시뮬레이션: 알고리즘의 성능 검증을 위한 백테스팅 기능
로그 및 모니터링: 시스템의 동작을 기록하고 문제를 진단할 수 있는 로깅 시스템
"""
