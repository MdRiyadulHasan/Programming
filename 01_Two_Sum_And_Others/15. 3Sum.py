from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum < 0:
                    l = l + 1
                elif currentSum > 0:
                    r = r - 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
        return res

# Example usage:
solution = Solution()
nums = [4,1,1,2,-1,5,2,-1-1,0,0,-2,2,-5,5,5]
result = solution.threeSum(nums)
print(result)
