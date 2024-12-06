from typing import List 
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        dic = Counter(arr)
        freq = sorted(dic.values(), reverse=True)
        print(freq)
        half = len(arr)//2
        size=0
        total = 0
        for n in freq:
            total+=n
            size+=1
            if total>=half:
                return size
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2