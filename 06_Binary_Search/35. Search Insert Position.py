# https://leetcode.com/problems/search-insert-position/description/
from typing import List 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif target<nums[m]:
                r = m-1
            else:
                l = l+1
        return l
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    ob = Solution()
    result = ob.searchInsert(nums, target)
    print(result)