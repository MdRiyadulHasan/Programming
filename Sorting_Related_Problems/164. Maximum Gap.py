class Solution:
    from typing import List 
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        maxdiff = 0
        for i in range(1, len(nums)):
            maxdiff = max(maxdiff, nums[i]-nums[i-1])
        return maxdiff
nums = [3,6,9,1]