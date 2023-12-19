from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1
        l = 0
        r = len(nums) - 1
        while l < r:
            currentSum = nums[l] + nums[r]
            if currentSum < k:
                res = max(currentSum, res)
                l = l + 1
            else:
                r = r - 1
        return res

solution = Solution()
nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
result = solution.twoSumLessThanK(nums, k)
print(result)
