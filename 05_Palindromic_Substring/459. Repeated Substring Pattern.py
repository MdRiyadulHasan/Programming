# https://leetcode.com/problems/repeated-substring-pattern/submissions/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len = len(s)
        rep = ""
        for i in range(s_len//2):
            rep +=s[i]
            if s_len%len(rep) == 0:
                if rep*(s_len//len(rep))==s:
                    return True
        return False     
ob = Solution()
s = "abcabcabcabc"
ans = ob.repeatedSubstringPattern(s)
print(ans)
