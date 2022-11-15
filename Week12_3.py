#3번 문제
import random

#행렬 생성 함수
def create_hang1 (m,n):
    line1 = []
    a = []
    
    for i in range(m):
        for j in range(n):
            line1.append(random.randint(1,9))
        a.append(line1)
        line1 = []
    return a

def create_hang2 (n,l):        
    line2 = []
    b = []
    for k in range(n):
        for t in range(l):
            line2.append(random.randint(1,9))
        b.append(line2)
        line2 = []       
    return b

#행렬 곱셈 함수
def cross_hang(A,B):
    n = len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C

v1 = int(input())
v2 = int(input())
v3 = int(input())
hang1 = create_hang1(v1,v2)
print(hang1)
hang2 = create_hang2(v2,v3)
print(hang2)

print(cross_hang(hang1,hang2))

