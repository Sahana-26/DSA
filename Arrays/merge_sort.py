def merge_sort(arr,low,high):
    while low < high:
        mid=(low + high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
    return arr

arr=[4,3,2,5,1]
n=len(arr)
low=0
high=n-1
print(merge_sort(arr,low,high))