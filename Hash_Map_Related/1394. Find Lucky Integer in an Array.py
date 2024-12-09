from typing import List 
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        freq_dic = Counter(arr)
        result = []
        for k,v in freq_dic.items():
            if k==v:
                result.append(k)
        return max(result) if result else -1