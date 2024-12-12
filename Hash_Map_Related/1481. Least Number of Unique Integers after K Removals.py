from typing import List 
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        freq_dic = Counter(arr)
        sorted_nums = sorted(freq_dic.values())
        print(sorted_nums)
        unique_count=len(sorted_nums)

        for count in sorted_nums:
            if k>=count:
                k-=count
                unique_count-=1
        return unique_count
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
