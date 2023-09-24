#check if 2 arrays are equal or not 

def equal(A,B,N):
    x={}
    for i in range(N):
        if A[i] in x.keys():
            x[A[i]]+=1
        else:
            x[A[i]]=1
    for i in range(N):
        if B[i] not in x.keys():
            return False
        x[B[i]]-=1
    for i in x.keys():
        if x[i]!=0:
            return False
    return True

# using sort()
def equal_using_sort(A,B,N):
    A.sort()
    B.sort()
    for i in range(N):
        if A[i]!=B[i]:
            return False
        else:
            return True

# using numpy
import numpy as np
def equal_using_numpy(A,B,N):
    A.sort()
    B.sort()
    if sum(np.subtract(A,B))!=0:
        return False
    if len(np.setdiff1d(B,A))!=0:
        return False
    if len(np.setdiff1d(A,B))!=0:
        return False
    return True

A=[2,4,6,8,10]
B=[3,5,6,8,10]
C=[2,4,6,8,10]
N=len(A)
print(equal(A,B,N))
print(equal_using_sort(A,C,N))
print(equal_using_numpy(B,C,N))