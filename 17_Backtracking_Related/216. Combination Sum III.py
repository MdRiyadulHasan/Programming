from typing import List 
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, current, currentSum):
            if len(current)==k and currentSum==n:
                result.append(current[:])
                return
            if len(current)>k or currentSum>n:
                return
            for i in range(start, 10):
                current.append(i)
                backtrack(i+1, current, currentSum+i)
                current.pop()
            
        result = []
        backtrack(1,[],0)
        return result
        