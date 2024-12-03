from typing import List 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if nums==sorted_nums:
            return 0
        l = 0
        r = len(nums)-1
        while l<r and nums[l]==sorted_nums[l]:
            l+=1
        while l<r and nums[r]==sorted_nums[r]:
            r-=1
        return r-l+1