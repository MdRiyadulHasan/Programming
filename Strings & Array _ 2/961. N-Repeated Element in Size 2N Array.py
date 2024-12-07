from typing import List 
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)//2
        nums_dic = Counter(nums)
        for k,v in nums_dic.items():
            if v==n:
                return k