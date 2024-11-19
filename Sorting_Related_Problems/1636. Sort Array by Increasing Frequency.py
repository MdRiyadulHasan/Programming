from typing import List 
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        dic = Counter(nums)
        result = sorted(dic.items(), key=lambda x:(x[1], -x[0]))
        result1 = [n for n,freq in result for _ in range(freq)]
        return result1
        