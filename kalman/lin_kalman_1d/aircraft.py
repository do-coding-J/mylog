import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from read_csv import *

alpha = 0.2
beta = 0.1
dt = 5   

def main():
    initial_pos = 30000 # m
    initial_vel = 40    # m/s
    result_pos = []
    result = []
    
    predict_pos, predict_vel = predict(initial_pos, initial_vel)

    file_name = '../aircraft.csv'
    data = read_csv(file_name)

    for measure in data:
        update_pos, update_vel = update(measure, predict_pos, predict_vel)
        predict_pos, predict_vel = predict(update_pos, update_vel)
        result_pos.append([measure, update_pos, predict_pos])
        result.append([round(measure,3), round(update_pos,3), round(update_vel,3), round(predict_pos,3), round(predict_vel,3)])
        
    for printable in result:
        print(printable)
        
    
def update(measure, pos, vel):
    new_pos = pos + (alpha * (measure - pos))
    new_vel = vel + (beta * ((measure - pos) / dt))

    return new_pos, new_vel

def predict(pos, vel):
    new_pos = pos + (dt * vel)
    new_vel = vel

    return new_pos, new_vel

if __name__ == "__main__":
    main()
    
'''
a-b filter (aircraft velocity)

이전에는 변하는 a값에 대하여이고
이번엔 고정된 a-b를 사용한다.

상황 : 
비행기의 거리를 측정하는 레이더가 있다.
이 레이더는 5초마다 한번씩 체크한다.
비행기는 30000m에서 시작해서 40m/s로 비행한다.
측정값에는 오차가 있다.
a-b인 이유는 위치와 속도 두가지를 구하기 때문에 허용 오차값이 두가지이기 떄문이다.

이전과 똑같이 x a,b를 사용하며 X a,b가 추가 되었다.

a = 0.2
b = 0.1

현재 위치 및 속도 업데이트
x0,0 (update) = 30000
X0,0 (update) = 40

현재 위치와 속도를 기반으로 다음 위치는 현재 위치 + (현재속도 * 다음 측정 시간)이다
속도에 대해서는 피드백이 없음으로 그대로 사용한다.
x1,0 (prediction) = x0,0 + (dt * X0,0) = 30000 + (5 * 40) = 30200
X1,0 (prediction) = X0,0 = 40

새로운 값으로 현재 위치와 속도를 업데이트 한다.
위치는 이전 예제와 동일한 state update formula를 사용하고
속도는 받는 값이 거리임으로 미분하여 속도로 변환 후 사용한다.
x1,1 (update) = x1,0 + a (z1 - x1,0) = 30200 + 0.2(30171 - 30200) = 30194.2
X1,1 (update) = X1,0 + b ( (z1 - x1,0) / dt) = 40 + 0.1 ( (30171 - 30200) / 5) = 39.42

다시 현재 위치와 속도를 기반으로 다음 위치를 계산한다.
속도에 대해서는 그대로 사용한다.
x2,1 (prediction) = x1,1 + (dt * X1,1) = 30194.2 + (5 * 39.42) = 30291.3
X2,1 (prediction) = X1,1 = 39.42

'''