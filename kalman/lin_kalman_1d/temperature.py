import sys
sys.path.append('../')
from read_csv import *

import matplotlib.pyplot as plt

def main():
    file = '../temperature.csv'
    raw_data = read_csv(file)
    names = raw_data[0]
    data = raw_data[1:]

    ploting = []
    true_val = []
    measure = []
    
    for index in range(0, len(data)):
        true_val.append(data[index][0])
        measure.append(data[index][1])
        # print(true_val[index], measure[index])
    

if __name__ == '__main__':
    main()