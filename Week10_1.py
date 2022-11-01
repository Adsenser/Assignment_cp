a = input().split(" ")
count = 0
for i in range(len(a)):
    if a[i] == 'the' or a[i]== 'the.' or a[i] == 'the,':
        count +=1 

print(count)
