from typing import List 
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter 
        nums_dic = Counter(nums)
        total = 0
        for k,v in nums_dic.items():
            if v==1:
                total+=k
        return total