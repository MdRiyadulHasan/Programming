# https://leetcode.com/problems/container-with-most-water/

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxArea = 0
        while l < r:
            area = min(height[l], height[r])*(r-l)
            maxArea = max(maxArea, area)
            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r-1
        return maxArea
ob = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = ob.maxArea(height)
print(result)