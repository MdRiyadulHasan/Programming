from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        result = []
        nums_count = Counter(nums)
        for k, v in nums_count.items():
            if v ==1:
                result.append(k)
        return result
