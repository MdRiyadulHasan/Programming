# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for ch in s:
            if ch in dic.values():
                stack.append(ch)
            else:
                if not stack or stack.pop()!=dic[ch]:
                    return False
        return len(stack)==0
ob = Solution()
s = "()[]{}"
result = ob.isValid(s)
print(result)

