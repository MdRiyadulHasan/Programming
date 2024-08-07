# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
from typing import List 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]==nums[r]:
                
                r=r-1
            elif nums[m]<nums[r]:
                r = m 
            else:
                l = m+1
        return nums[l]
ob = Solution()
nums =[1,3,3]
res = ob.findMin(nums)
print(res)