from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if abs(currentSum - target) < abs(closest - target):
                    closest = currentSum
                if currentSum < target:
                    l = l + 1
                else:
                    r = r - 1
        return closest

solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
result = solution.threeSumClosest(nums, target)
print(result)
