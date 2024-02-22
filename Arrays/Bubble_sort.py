def Bubble(a):
    for i in range(0,len(a)):
        for j in range(1,len(a)-i):
            if a[j]<a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
    return a

a=[3,2,1,5,4]
print(Bubble(a))

            