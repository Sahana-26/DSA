def kth_min_max(a,k,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j] = a[j],a[i]
    print(a)
    print("k'th min: ", a[k-1])
    print("k'th max: ", a[n-k])

arr=[]
n= int(input("enter number of digits: "))
print("enter digit: ")

for i in range(n):
    a=input()
    arr.append(a)
k=int(input("enter k: "))
print("array: ",arr)

kth_min_max(arr,k,n)