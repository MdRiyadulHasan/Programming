# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 3
        for i in range(3, len(nums)):
            if nums[i]!=nums[k-3]:
                nums[k]=nums[i]
                k=k+1
        return k
nums = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,5,6,7,7,7,7,8]
ob = Solution()
result = ob.removeDuplicates(nums)
print(result)