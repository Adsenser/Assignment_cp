inStr = ''
inList = []
score_eng = []
score_mat = []
score_phy = []

with open('/Users/ehoi/Downloads/input_data.txt','r',encoding= 'UTF-8') as inFp:
    inFp.readline()
    icount = 0
    while True:
        inStr = inFp.readline()
        if inStr == '':
            break
        inList = inStr.split()

        score_eng.append(int(inList[2]))
        score_mat.append(int(inList[3]))
        score_phy.append(int(inList[4]))
        icount += 1

print("영어",sum(score_eng)/icount)
print("수학",sum(score_mat)/icount)
print("물리",sum(score_phy)/icount)
