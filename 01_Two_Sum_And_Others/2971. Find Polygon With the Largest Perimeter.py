# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/

from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans
ob = Solution()
nums = [1,12,1,2,5,50,3]
res = ob.largestPerimeter(nums)
print(res)