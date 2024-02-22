def calcGCD(n:int, m: int) -> int:
    a=[]
    for i in range(1,max(n,m)):
        if n%i==0 and m%i==0:
            a.append(i)
    return max(a)
n=int(input())
m=int(input())
print(calcGCD(n,m))