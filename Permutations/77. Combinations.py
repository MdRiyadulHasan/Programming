from typing import List 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(nums,path):
            if len(path)==k:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[i+1:], path+[nums[i]])

        backtrack(list(range(1,n+1)), [])
        return res
n = 4
k = 2
ob = Solution()
result = ob.combine(n,k)
print(result)

        