from typing import List 
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)<2:
            return -1
        max_num = max(nums)
        max_index = nums.index(max_num)
        for i,n in enumerate(nums):
            if i!=max_index and max_num<2*n:
                return -1
        return max_index