from typing import List 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n = len(nums)
        nums_dic = Counter(nums)
        threshold = n//3
        result = [k for k, v in nums_dic.items() if v>threshold]
        return result