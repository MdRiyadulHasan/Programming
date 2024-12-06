from typing import List 
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_count = 1
        current_count = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current_count+=1
                max_count = max(max_count, current_count)
            else:
                current_count=1
        return max_count