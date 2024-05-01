# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]<target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1

nums = [4,5,6,7,0,1,2],
target = 0


        