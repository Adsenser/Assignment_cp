import math
a = 1
b = 1/2
sum_result = 0
count = int(input())

for n in range(1,count+1):
    p_a = ((a*((math.sqrt(2)/2)**(n-1)))**2)
    p_b = ((b*((math.sqrt(2)/2)**(n-1)))**2)*math.pi
    result = p_a - p_b
    sum_result +=result
    print(sum_result)
