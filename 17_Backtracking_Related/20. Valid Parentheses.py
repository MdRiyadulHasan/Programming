class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "}":"{", "]":"["}
        for ch in s:
            if ch in dic.values():
                stack.append(ch)
            else:
                if not stack or stack.pop()!=dic[ch]:
                    return False
        return len(stack)==0
        
s = "([])"   
ob = Solution()
ans = ob.isValid(s)
print(ans)