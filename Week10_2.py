a = map(int,input().split(";"))
a = list(a)
a = a[::-1]
for b in a:
    print(
        f"{b:9,d}"
    )
