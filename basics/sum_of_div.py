def sumOfAllDivisors(n):
    a=[]
    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%j==0:
                count+=j
        a.append(count)
        count=0
    return sum(a)
        
n=int(input())
print(sumOfAllDivisors(n))