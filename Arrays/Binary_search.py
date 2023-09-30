def binary_search(a,low,high,x):
    if high>=low:
        mid = (high+low)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            binary_search(a,mid+1,high,x)
        else:
            binary_search(a,low,mid-1,x)
    else:  
        return -1   
    
a= [2,5,3,8,1,9]
print(a)
a.sort()
low=0
high=len(a)-1
x=int(input("enter element to be searched: "))
print(binary_search(a,low,high,x))

