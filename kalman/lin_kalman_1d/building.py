import sys
sys.path.append('../')
from read_csv import *

import matplotlib.pyplot as plt

measure_error = 5
human_error = 15

def main():
    true_val = 50
    intial_val = 60
    
    result = []
    result_kn = []
    
    predict_height, predict_error = predict(intial_val, pow(human_error, 2))
    
    file = '../building.csv'
    data = read_csv(file)
    
    for index in range(0, len(data)):
        Kn, update_height, update_error = update(data[index][0], predict_height, predict_error)
        predict_height, predict_error = predict(update_height, update_error)
        result.append([true_val, predict_height, update_height, data[index][0]])
        result_kn.append([Kn])
        
    
    # plt.plot(result_kn)
    
    plt.plot(result)
    plt.legend(['true', 'estimate', 'update', 'measure'])
    
    plt.show()
    
def predict(height, error):
    new_h = height
    new_e = error
    return new_h, new_e

def update(measure, height, error):
    new_Kn = error / (error + pow(measure_error,2))
    new_state = height + new_Kn * (measure - height)
    new_error = (1-new_Kn) * error
    return new_Kn, new_state, new_error

if __name__ == '__main__':
    main()
    
'''
constant value with measureing error
'''