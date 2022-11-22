import numpy as np
import random

def print_mat(A):
    nrow = len(A)
    ncol = len(A[0])
    for i in range(nrow):
        for j in range(ncol):
            print(A[i][j],end=' ')
        print('')
    print('')

def init_mat(m,n,ini='zero'):
    A = []
    for i in range(m):
        tmp = []
        for j in range(n):
            if ini =='zero':
                tmp.append(0)
            else:
                value = random.randint(1,9)
                tmp.append(value)

        A.append(tmp)
    return A

def mat_mult(A,B):
    nrow = len(A)
    ncol = len(B[0])
    n1 = len(A[0])
    n2 = len(B)
    if n1 != n2:
        print("Error")
        return -999;

    C = init_mat(nrow,ncol,ini='zero')
    for i in range(nrow):
        for j in range(ncol):
            value = 0
            for k in range(n1):
                value += A[i][k] * B[k][j]
            C[i][j] = value
    return C

m,n,l = map(int,input('m,n,l:').split(","))

A = init_mat(m,n,ini='random')
arr_A = np.array(A)

B = init_mat(n,l,ini='random')
arr_B = np.array(B)

C = mat_mult(A,B)

print("A=")
print_mat(A)

print("B=")
print_mat(B)

print("maanual C=")
print_mat(C)
