from typing import List 
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for nums_list in nums[1:]:
            common&=set(nums_list)   
        return sorted(common)
        