# https://leetcode.com/problems/combination-sum/description/

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(candidates, target, path):
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    continue
                backtrack(candidates[i:], target-candidates[i], path+[candidates[i]])
        backtrack(candidates, target, [])
        return res
candidates = [2,3,6,7]
target = 7
ob = Solution()
result = ob.combinationSum(candidates,target)
print(result)