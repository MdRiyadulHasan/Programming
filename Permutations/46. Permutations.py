# https://leetcode.com/problems/permutations/

from typing import List 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]])

        backtrack(nums,[])
        return res
nums = [1,2,3]
ob = Solution()
result = ob.permute(nums)
print(result)