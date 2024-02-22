def sortedArray(a: [int], b: [int]) -> [int]:
    dict={}
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in b:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return list(dict.keys())
a=[1,2,2,3,4,4]
b=[4,3,5,6,6]
print(sortedArray(a,b))