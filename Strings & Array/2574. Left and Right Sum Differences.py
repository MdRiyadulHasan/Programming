from typing import List 
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        suffix = sum(nums)
        prefix = 0 
        ans = []
        for n in nums:
            prefix+=n   
            ans.append(abs(prefix-suffix))
            suffix-=n 
        return ans