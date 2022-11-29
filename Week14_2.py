import pickle
import os.path

inFp = open("/Users/ehoi/Documents/GitHub/Baekjoon/input_data.txt")
inList = inFp.readlines()
line1 = inList[0]
c = []
for i in range(1,11):
    a = inList[i]
    b = a.split()
    b[0] = int(b[0])
    b[2] = int(b[2])
    b[3] = int(b[3])
    b[4] = int(b[4])
    c.append(b)
with open("/Users/ehoi/Documents/GitHub/Baekjoon/input_data1.txt", 'wb') as file:
    pickle.dump(line1, file)
    for j in range(len(c)):
        pickle.dump(c[j], file)
with open("/Users/ehoi/Documents/GitHub/Baekjoon/input_data1.txt",'rb') as file:
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)
    data = pickle.load(file)
    print(data)

print("원본 파일 크기:",os.path.getsize("/Users/ehoi/Documents/GitHub/Baekjoon/input_data.txt"),"byte")
print("Pcikle 이후 크기:",os.path.getsize("/Users/ehoi/Documents/GitHub/Baekjoon/input_data1.txt"),"byte")
inFp.close
