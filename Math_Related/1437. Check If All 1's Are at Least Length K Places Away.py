from typing import List 
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one_index = -1
        for i, n in enumerate(nums):
            if n==1:
                if prev_one_index!=-1 and i-prev_one_index-1<k:
                    return False
                prev_one_index=i
        return True