import sys
sys.path.append("../")
from read_csv import *

def main():
    data = []
    file = '../csv/vehicle_localization.csv'
    raw = read_csv(file)
    for raw_data in raw:
        data.append(int)

if __name__=="__main__":
    main()