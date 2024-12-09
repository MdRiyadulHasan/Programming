from typing import List 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_dic = {}
        for i,n in enumerate(sorted_nums):
            if n not in num_dic:
                num_dic[n]=i
        return [num_dic[num] for num in nums]