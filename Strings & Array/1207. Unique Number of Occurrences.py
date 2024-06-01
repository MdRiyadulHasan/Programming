from typing import List 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter 
        freq = Counter(arr)
        return len(freq)==len(set(freq.values()))
arr = [1,2,2,1,1,3]