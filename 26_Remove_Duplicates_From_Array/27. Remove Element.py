# https://leetcode.com/problems/remove-element/

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k = k+1
        return k
nums = [3,2,2,3]
val = 3
ob = Solution()
result = ob.removeElement(nums,val)
print(result)