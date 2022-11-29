inFp = open("/Users/ehoi/Documents/GitHub/Baekjoon/input_data.txt")
eng = []
math = []
phy = []
inList = inFp.readlines()
for i in range(1,11):
    a = inList[i]
    b = a.split()
    eng.append(int(b[2]))
    math.append(int(b[3]))
    phy.append(int(b[4]))

eng_mean = sum(eng)/len(eng)
math_mean = sum(math)/len(math)
phy_mean = sum(phy)/len(phy)

print("영어평균:", eng_mean)
print("수학평균:", math_mean)
print("물리평균:", phy_mean)
inFp.close
