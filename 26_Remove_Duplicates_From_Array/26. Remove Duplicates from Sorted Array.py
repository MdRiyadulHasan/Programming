# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i-1]!=nums[i]:
                nums[k] = nums[i]
                k = k+1
        return k
nums = [0,0,1,1,1,2,2,3,3,4]
ob = Solution()
result = ob.removeDuplicates(nums)
print(result) 