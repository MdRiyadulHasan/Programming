# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return True
            elif nums[m]==nums[l]==nums[r]:
                l = l+1
                r = r-1
            elif nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]<target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False

nums = [2,5,6,0,0,1,2]
target = 0