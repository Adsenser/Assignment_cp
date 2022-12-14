inFp = open("/Users/ehoi/Documents/GitHub/Baekjoon/input_data.txt","r")

inList = inFp.readlines()
sum = []
line = []
for i in range(1,11):
    a = inList[i]
    b = a.split()
    temp_sum = int(b[2])+int(b[3])+int(b[4])
    sum.append(temp_sum)

a = inList[0]
b = a.split()
for j in range(0, 5):
    line.append(b[j])
line.append('Total')
# print(line)

real2_line = []
for i in range(1,11):
    real_line = []
    temp_line = []
    for j in range(0,5):
        a = inList[i]
        b = a.split()
        temp_line.append(b[j])
    real_line.extend(temp_line)
    real_line.append(sum[i-1])
    # print(real_line)
    real2_line.append(real_line)

# print(real2_line)
for i in line:
    print(f'{i:<10}',end="")
print()
for j in real2_line:
    for k in range(len(j)):
        print(f'{j[k]:<10}',end="")
    print()
