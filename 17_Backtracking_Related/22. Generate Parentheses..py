class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def backtrack(open,close,curStr):
            if len(curStr)==2*n:
                res.append(curStr)
                return
            if open<n:
                backtrack(open+1, close, curStr+"(")
            if close<open:
                backtrack(open, close+1, curStr+")")
            
        backtrack(0,0,"")
        return res