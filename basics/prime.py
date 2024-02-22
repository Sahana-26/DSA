n=int(input())
flag=False
if n==1:
    print("NO")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
 
if flag==True:
    print("no")
else:
    print("yes")