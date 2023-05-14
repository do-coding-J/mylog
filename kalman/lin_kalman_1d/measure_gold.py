import csv
import matplotlib.pyplot as plt

def main():
    step = 0
    initial_val = 1000

    file = '../gold.csv'
    data = []
    
    result = []
    
    with open(file, newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ')
        for row in csv_reader:
            data.append(int(row[0]))
            
    for measure in data:
        step = step + 1
        if step == 1:
            prev_prediction = initial_val
        gain = 1/step
        current_estimation = prev_prediction + gain * (measure - prev_prediction)
        prev_prediction = current_estimation
        # result.append([step, round(gain,3), measure, round(current_estimation,3), round(prev_prediction,3)])
        result.append([initial_val, measure, round(current_estimation,3), round(prev_prediction,3)])        
    for printable in result:
        print(printable)

    plt.plot(result)
    plt.legend(['true value', 'measure', 'current', 'prev'])
    plt.xlabel('Iterations')
    plt.ylabel('weight')
    plt.show()

if __name__ == '__main__':
    main()

'''
1번 예제
금 무게 재기

여기에선 금의 무게를 측정 했을 때 측정 값에 에러가 있을 경우를 예시로 한다.
X a,b로 표기한다. 
X는 계산 중인 대상
a는 next predict단계를,
b는 update단계를 나타낸다.

true value가 1000일 때

x0,0 아무것도 없기에 initial value를 사용한다. (시작 값)
x1,0 금의 무게는 변하지 않음으로 다음 예측은 현재 값을 사용한다. x1,0 = x0,0 = 1000

gain 값을 먼저 구한다. 1번 째 측정임으로 a1 = 1/1이 된다.
측정 값은 z1 = 996이다.
x1,1 = x1,0 + a1(z1 - x1,0) = 1000 + 1/1(996-1000) = 996 이 된다.
x2,1 금의 무게는 변하지 않음으로 다음 예측은 현재 값을 사용한다. x2,1 = x1,1 = 996

a2 = 1/2, z2 = 994
x2,2 = x2,1 + a2(z2 - x2,1) = 996 + 1/2(994 - 996) = 995
x3,2 = x2,2 = 995

.
.
.

a10 = 1/10, z10 = 1023
x10,10 = 996.67 + 1/10(1023 - 996.67) = 999.3
'''