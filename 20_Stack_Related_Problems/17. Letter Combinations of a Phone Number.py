# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans = []
        def backtrack(i,curStr):
            if len(digits)==len(curStr):
                ans.append(curStr)
                return
            for c in dic[digits[i]]:
                backtrack(i+1, curStr+c)
        if digits:
            backtrack(0,'')
        return ans
ob = Solution()
digits = "23"
result = ob.letterCombinations(digits)
print(result)