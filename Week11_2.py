import random
a = []
for _ in range(10):
    a.append(random.randint(1,100))
print("초기 리스트",a)

for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            b1 = a[i+1]
            b2 = a[i]
            a.insert(i,b1)
            del a[i+1]
            a.insert(i+1,b2)
            del a[i+2]
            print(a)
