#난수 생성 후 리스트 저장 파트
import random
a = []
for _ in range(10):
    a.append(random.randint(1,100))
print(a)
# 최댓값, 최솟값 탐색 파트
max = 0
max_index = 0
min = 100
min_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    elif a[i] < min:
        min = a[i]
        min_index = i
    elif a[i] == min or a[i] == max:
        continue

print("최댓값:",max,"리스트 번호:",max_index)
print("최솟값:",min,"리스트 번호:",min_index)
