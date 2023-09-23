arr=[]
n= int(input("enter number of digits: "))
print("enter digit: ")
for i in range(n):
    a=input()
    arr.append(a)
print("array: ",arr)

def reverse(a,start,end):
    while start<=end:
        a[start],a[end]=a[end],a[start]
        start+=start
        end-=end
        return a

print(reverse(arr,0,n-1))