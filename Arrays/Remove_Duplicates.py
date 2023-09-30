def removeDuplicates(nums):
        a=[]
        for num in nums[::-1]:
            print(a)
            if num not in a:
                a.append(num)
                print(a)
            else:
                nums.remove(num)
                print(nums)
        return len(a)

nums = [1,2,2,2,2,3]
ans = removeDuplicates(nums)
print(ans)