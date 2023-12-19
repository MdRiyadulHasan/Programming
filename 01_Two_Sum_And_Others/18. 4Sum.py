from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l = l + 1
                    elif total > target:
                        r = r - 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        l = l + 1
                        r = r - 1
        return res

# Example usage:
solution = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = solution.fourSum(nums, target)

print(result)
