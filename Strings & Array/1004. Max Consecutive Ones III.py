from typing import List 
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxCount = 0
        dic = {0:0, 1:0}
        for r, n in enumerate(nums):
            dic[n]+=1 
            while dic[0]>k:
                dic[nums[l]]-=1 
                l+=1 
            maxCount = max(maxCount, r-l+1)
        return maxCount
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2