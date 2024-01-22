# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccurance(nums,target):
            result = -1
            l = 0
            r = len(nums)-1
            while l<=r:
                m = (l+r)//2
                if nums[m]==target:
                    result = m
                    r = m-1
                elif nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return result
        def lastOccurance(nums,target):
            result = -1
            l = 0
            r = len(nums)-1
            while l<=r:
                m = (l+r)//2
                if nums[m]==target:
                    result = m
                    l = m+1
                elif nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return result
            
        first = firstOccurance(nums,target)
        last = lastOccurance(nums,target)
        return [first, last]