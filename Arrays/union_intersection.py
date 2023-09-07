# union and intersection of arrays

def printUnion(a, n,  b, m):
    mp = {}
 
    # Inserting array elements in mp
    for i in range(n):
        mp[a[i]] = i
 
    for i in range(m):
        mp[b[i]] = i
 
    print("The union set of both arrays is : ")
    for key in mp.keys():
 
        print(key, end=" ")
    
    
def intersect(a,b):
    m = {}
    if len(a)<len(b):
        a,b = b,a
    for i in a:
        if i not in m:
            m[i] = 1
        else:
            m[i]+=1
    result = []
    for i in b:
        if i in m and m[i]:
            m[i]-=1
            result.append(i)
    return result


def intersect1(a,b):
    print("intersection :")
    for i in b:
        if i in a:
            print(i, end=" ")
            
            
a = [1, 2, 5, 6, 2, 3, 5]
b = [2, 4, 5, 6, 8, 9, 4, 6, 5]
 
printUnion(a, 7, b, 9)
intersect(a,b)
intersect1(a,b)