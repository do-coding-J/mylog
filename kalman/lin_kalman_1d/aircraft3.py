import sys
sys.path.append('../')
from read_csv import *

import matplotlib.pyplot as plt

a = 0.5
b = 0.4
c = 0.1
dt = 5

def main():
    file = '../aricraft3.csv'
    data = read_csv(file)
    result_pos = []
    result_vel = []
    result_acc = []
    
    predict_pos, predict_vel, predict_acc = predict(30000, 50, 0) # 0 predict
    
    for index in range(0, len(data)):
        update_pos, update_vel, update_acc = update(data[index][0], predict_pos, predict_vel, predict_acc)
        predict_pos, predict_vel, predict_acc = predict(update_pos, update_vel, update_acc)
        result_pos.append([round(update_pos,3), round(predict_pos,3), data[index][0]])
        result_vel.append([round(update_vel,3), round(predict_vel,3), data[index][1]])
        result_acc.append([round(update_acc,3), round(predict_acc,3), data[index][2]])
        
    for printable in range(0, len(data)):
        print(result_pos[printable] + result_vel[printable] + result_acc[printable])
    
    # plt.plot(result_pos)
    # plt.plot(result_vel)
    # plt.plot(result_acc)
    
    # plt.legend(['update', 'predict', 'ture'])
    # plt.show()
    
    
def update(measure, pos, vel, acc):
    new_pos = pos + a * (measure - pos)
    new_vel = vel + b * ((measure - pos)/dt)
    new_acc = acc + c * ((measure - pos) / (0.5 * pow(dt, 2)))
    return new_pos, new_vel, new_acc
        
def predict(pos, vel, acc):
    new_pos = pos + (vel * dt) + (acc * pow(dt, 2) / 2)
    new_vel = vel + (acc * dt)
    new_acc = acc
    return new_pos, new_vel, new_acc


if __name__ == '__main__':
    main()