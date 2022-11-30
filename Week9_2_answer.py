a = []
b = []
c = {}
a = input().split(" ")
b = input().split(" ")

for i in range(len(a)):
    c[a[i]] = b[i]
#delta 인 키-값 쌍 삭제
del c['delta']
#값이 30인 키-값 쌍 삭제
d = dict(zip(c.values(),c.keys()))
del d['30']
c = dict(zip(d.values(),d.keys()))
print(c)
