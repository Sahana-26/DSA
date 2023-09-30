def searchRange(nums, target):
        a=[]
        '''for num in nums:
            if num==target :
                x=nums.index(num)
                a.append(x)
                break
        for num in nums[::-1]:
            if num==target :
                x=nums.index(num)
                a.append(x)
                break'''
        if target in nums:
            a1=a.index(target)
            a.append(a1)
            a.reverse()
            a2=a.index(target)
            a.append(a2)
            return a
        else:
              return [-1,-1]
        

nums = [5,7,7,8,8,10]
target = 8
ans = searchRange(nums, target)
print(ans)