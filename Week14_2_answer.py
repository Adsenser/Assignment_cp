import os.path
import pickle

inStr = ''
inList = []

with open('/Users/ehoi/Downloads/input_data.txt','r',encoding= 'UTF-8') as inFp:
    with open('/Users/ehoi/Downloads/output.bin', 'wb') as  outFp:
        inStr = inFp.readline()
        pickle.dump(inStr,outFp)
        icount = 0
        while True:
            inStr = inFp.readline()
            if inStr == '':
                break
            inList = inStr.split()
            tmp = [int(inList[0]),inList[1],int(inList[2]),int(inList[3]),int(inList[4])]
            pickle.dump(tmp,outFp)
            icount += 1

with open('/Users/ehoi/Downloads/output.bin','rb') as inFp:
    print(pickle.load(inFp))
    for i in range(icount):
        print(pickle.load(inFp))

print("원본 파일 크기:",os.path.getsize('/Users/ehoi/Downloads/input_data.txt'),"byte")
print("Pcikle 이후 크기:",os.path.getsize('/Users/ehoi/Downloads/output.bin'),"byte")
