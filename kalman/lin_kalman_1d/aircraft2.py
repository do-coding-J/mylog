import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from read_csv import *

a = 0.2
b = 0.1
dt = 5

def main():
    file = '../aircraft2.csv'
    data = read_csv(file)
    
    result_update = []
    result_predict = []
    result_pos = []
    result_vel = []
    initial_pos = 30000
    initial_vel = 50
    vel = initial_vel
    increase_vel = 8 * dt
    predict_pos, predict_vel = predict(initial_pos, initial_vel)

    for measure in range(0,len(data)):
        update_pos, update_vel = update(data[measure][0], predict_pos, predict_vel)
        predict_pos, predict_vel = predict(update_pos, update_vel)
        result_update.append([round(update_pos,3), round(update_vel,3)])
        result_predict.append([round(predict_pos,3), round(predict_vel,3)])
        result_pos.append([data[measure][0], round(update_pos,3), round(predict_pos,3)])
        if measure < 5:
            result_vel.append([vel, round(update_vel,3), round(predict_vel,3)])
        else:
            vel = vel + increase_vel
            result_vel.append([vel, round(update_vel,3), round(predict_vel,3)])
                
    # for printable in range(0, len(result_update), 1):
    #     print(str(data[printable]) + '\t' + str(result_update[printable]) + '\t' + str(result_predict[printable]))

    # plt.plot(result_pos)
    
    plt.plot(result_vel)
    
    plt.legend(['measure','update', 'predict'])
        
    
    plt.show()
    
def update(measure, pos, vel):
    new_pos = pos + (a * (measure - pos))
    new_vel = vel + (b * ((measure - pos) / dt))
    return new_pos, new_vel
    
def predict(pos, vel):
    new_pos = pos + (vel * dt)
    new_vel = vel
    return new_pos, new_vel
    
if __name__ == '__main__':
    main()
    
'''
속도가 변하는 비행기

이번에는 중간에 속도가 변하는 비행기다.
첫 20초는 등속비행 하다 남은 시간동안은 8m/s/s으로 가속하는 비행기이다.
a = 0.2, b = 0.1, dt = 5이므로 20초 뒤 비행기의 속도는 측정마다 40m/s씩 증가한다.

이전 예제와 같은 방식으로 진행한다.
x a,b와 X a,b를 사용하고 위치와 속도를 나타낸다. 속도는 위치에 시간을 나눠 사용한다.

상태와 속도 업데이트는 이전과 같은 공식을 사용한다.
예측 또한 같은 공식을 사용한다.

여기서 봐야 할 점은 leg error이다.
leg error는 아래와 같이 불리기도 한다.
- dynamic error
- system error
- bias error
- truncation error

'''