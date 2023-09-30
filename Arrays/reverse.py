def reverse(a,start,end):
    while start<=end:
        a[start],a[end]=a[end],a[start]
        start+=start
        end-=end
        return a

#Using slicing
def reverse_slicing(a):
    print(a[::-1])
    return a

arr=[]
n= int(input("enter number of digits: "))
print("enter digit: ")

for i in range(n):
    a=input()
    arr.append(a)
print("array: ",arr)

print("reversed array : ",reverse(arr,0,n-1))
print("reversed array : ",reverse_slicing(arr))