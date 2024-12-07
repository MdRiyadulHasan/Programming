class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []
        for ch in s:
            if ch=="(":
                if stack:
                    result.append("(")
                stack.append("(")
            else:
                stack.pop()
                if stack:
                    result.append(")")
                
        return "".join(result)