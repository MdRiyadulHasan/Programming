from typing import List 
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = [x for x in nums if x<0]
        if 0 in nums:
            return 0
        elif len(negative)%2!=0:
            return -1
        else:
            return 1
