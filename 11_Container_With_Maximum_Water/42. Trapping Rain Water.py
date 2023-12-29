# https://leetcode.com/problems/trapping-rain-water/submissions/

from typing import List 
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lMax =0
        rMax = 0
        trapedWater = 0
        while l < r:
            if height[l]<=height[r]:
                if height[l]>=lMax:
                    lMax = height[l]
                else:
                    trapedWater+=lMax-height[l]
                l = l + 1
            else:
                if height[r]>=rMax:
                    rMax = height[r]
                else:
                    trapedWater+=rMax-height[r]
                r = r-1
        return trapedWater       
ob = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = ob.trap(height)
print(result)