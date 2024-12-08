from typing import List 
class Solution:
    def check(self, nums: List[int]) -> bool:
        count_decreasing = 0
        n = len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count_decreasing+=1
            if count_decreasing>1:
                return False
        return True