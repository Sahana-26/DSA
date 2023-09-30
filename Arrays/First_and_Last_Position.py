def searchRange(nums, target):
        result = []
        if target in nums:
            first_index = nums.index(target)
            result.append(first_index)
            last_index = len(nums) - 1 - nums[::-1].index(target)
            result.append(last_index)
            return result
        else:
            return [-1, -1]
        

nums = [5,7,7,8,8,10]
target = 8
ans = searchRange(nums, target)
print(ans)