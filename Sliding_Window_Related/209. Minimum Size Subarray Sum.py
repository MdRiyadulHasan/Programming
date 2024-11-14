from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_length = float('inf')
    left = 0
    cur_sum = 0
    for right in range(len(nums)):
        cur_sum+=nums[right]
        while cur_sum>=target:
            min_length = min(min_length, right-left+1)
            cur_sum-=nums[left]
            left+=1
    return min_length if min_length!=float('inf') else 0
    
    
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))