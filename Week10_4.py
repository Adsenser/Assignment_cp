a = input()
es = ''
el = ''
n = ''
h = ''
etc = ''

for i in range(len(a)):
    if a[i].isupper() == True:
        es += a[i]
    elif a[i].islower() == True:
        el += a[i]
    elif a[i].isdigit() == True:
        n += a[i]
    elif 44032<= ord(a[i]) <= 55203:
        h += a[i]
    else:
        etc += a[i]

print(es)
print(el)
print(n)
print(h)
print(etc)
