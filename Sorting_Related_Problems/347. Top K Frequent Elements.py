from typing import List 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        dic = Counter(nums)
        # Sort by frequency and take the top k elements
        result = list(sorted(dic, key=lambda x: dic[x], reverse=True))[:k]
        return result