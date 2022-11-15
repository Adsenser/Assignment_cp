#2번 문제 -1
import random
import pandas as pd

def ran_int (n):
    b = []
    for _ in range(n):
        b.append(random.randint(1,100))
    return b

a = ran_int(1000)
#조건1 검증 - 1단계: 도수분포표 생성 알고리즘
count1=0;count2=0;count3=0;count4=0;count5=0;count6=0;count7=0;count8=0;count9=0;count10=0
for i in range(1000):
    if 0<a[i]<=10 :
        count1 +=1
    elif 10<a[i]<=20 :
        count2 += 1
    elif 20<a[i]<=30 :
        count3 += 1
    elif 30<a[i]<=40 :
        count4 += 1
    elif 40<a[i]<=50 :
        count5 += 1
    elif 50<a[i]<=60 :
        count6 += 1
    elif 60<a[i]<=70 :
        count7 += 1
    elif 70<a[i]<=80 :
        count8 += 1
    elif 80<a[i]<=90 :
        count9 += 1
    elif 90<a[i]<=100:
        count10 +=1
#(x-1)//10 를 이용해 몫이 뭐냐에 따라 카운트 값 다르게 적용가능함. 이를 이용시 간결하게 코드 짤 수 있음.
    
result = [count1,count2,count3,count4,count5,count6,count7,count8,count9,count10]
r = ["1-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100"]
table = pd.DataFrame({"range" :r, "count" :result})
table

#생성된 도수분포표를 이용해 Matplotlib 막대 그래프 그리기 
#주피터 노트북 이용시 새로운 란에 작성
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.bar(x, result)
plt.xticks(x, r)

plt.show()

#생성된 도수분포표를 이용해 Matplotlib 막대 그래프 그리기 ㄴㅗ트
#생성된 도수분포표를 이용해 Matplotlib 막대 그래프 그리기 
