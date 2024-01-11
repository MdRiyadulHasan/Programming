# https://leetcode.com/problems/combination-sum-ii/description/ 

from typing import List 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(candidates, target, path):
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    continue
                if i>0 and candidates[i]==candidates[i-1]:
                    continue
                backtrack(candidates[i+1:], target-candidates[i], path+[candidates[i]])
        backtrack(candidates, target, [])
        return res
candidates = [10,1,2,7,6,1,5]
target = 8
ob = Solution()
result = ob.combinationSum2(candidates, target)
print(result)