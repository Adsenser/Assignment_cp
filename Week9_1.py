a, b = map(int,input().split(" "))
c = []
for i in range(a,b+1):
    k = 2**i
    c.append(k)

print(c)
