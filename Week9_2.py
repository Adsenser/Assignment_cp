a = []
b = []
c = {}
a = input().split(" ")
b = input().split(" ")

for i in range(len(a)):
    c[a[i]] = b[i]

del c['delta']
del c['alpha']

print(c)
