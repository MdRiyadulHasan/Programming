from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        minProduct = nums[0]*nums[1]
        maxProduct = nums[-1]*nums[-2]
        return maxProduct-minProduct
# Input: nums = [5,6,2,7,4]
# Output: 34