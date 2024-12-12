from typing import List 
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        num_dic = Counter(nums)
        result = []
        for k, v in num_dic.items():
            if v==2:
                result.append(k)
        return result