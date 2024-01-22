# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List 
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, n in enumerate(sorted(nums)):
            if target == n:
                ans.append(i)
        return ans