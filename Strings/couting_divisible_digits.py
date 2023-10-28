def countDigits(n: int) -> int:
    n=str(n)
    digits=0
    for i in n:
        m=int(n)
        i=int(i)
        if i==0:
            continue
        if m%i==0:
            digits+=1
    return digits

#n=int(input("enter n : "))
print(countDigits(373))