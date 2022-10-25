import random

m = int(input())
n = int(input())
l = int(input())

line1 = []
a = []

for i in range(m):
    for j in range(n):
        line1.append(random.randint(1,9))
    a.append(line1)
    line1 = []

line2 = []
b = []
for k in range(n):
    for t in range(l):
        line2.append(random.randint(1,9))
    b.append(line2)
    line2 = []

result = 0
semi_final = []
real_final = []

for i in range(m):
    for k in range(l):
        for j in range(n):
            aa = a[i][j]
            bb = b[j][k]
            result += aa*bb
        semi_final.append(result)
        result = 0
    real_final.append(semi_final)
    semi_final = []

print(real_final)

#넘파이 모듈과의 비교

import numpy as np
arr1 = np.array(a)
arr2 = np.array(b)
arr_mul = arr1 @ arr2
print(arr_mul)
