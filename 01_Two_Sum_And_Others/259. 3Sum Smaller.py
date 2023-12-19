from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum < target:
                    # If the current sum is less than the target, all pairs in the range (l, r) will also satisfy the condition
                    count = count + r - l
                    l = l + 1
                else:
                    r = r - 1
        return count

solution = Solution()
nums = [-2, 0, 1, 3]
target = 2
result = solution.threeSumSmaller(nums, target)
print(result)
