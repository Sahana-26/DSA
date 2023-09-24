#inbuilt functions
def min_max(arr):
    print("min: ", min(arr))
    print("max: ", max(arr))

#user defined function
def min_max_arr(a,n):
    if n==1:
        min=a[0]
        max=a[0]
        print("min: ", min , "max: ", max)
    else:
        if a[0]>a[1]:
            min=a[1]
            max=a[0]
        else:
            max=a[1]
            min=a[0]
        for i in range(2, n):
            if a[i]>max:
                max=a[i]
            elif a[i]<min:
                min=a[i]
    print("min: ", min , "max: ", max)

arr=[]
n= int(input("enter number of digits: "))
print("enter digit: ")

for i in range(n):
    a=input()
    arr.append(a)
print("array: ",arr)

min_max_arr(arr,n)
