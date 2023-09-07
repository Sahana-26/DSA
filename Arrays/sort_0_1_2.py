# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

def sort(arr,n):
        low=0
        high=n-1
        mid=0
        while mid<=high:
            if arr[mid]==0:
                arr[mid] , arr[low] = arr[low] , arr[mid]
                mid+=1
                low+=1
            
            elif arr[mid]==1:
                mid+=1
            
            else:
                arr[mid] , arr[high] = arr[high] , arr[mid]
                high-=1
        return arr
                
def pr(arr):
    for i in arr:
        print(i,end=' ')

n=7
a=[0,2,2,1,2,0,2]
a=sort(a,7)
pr(a)
