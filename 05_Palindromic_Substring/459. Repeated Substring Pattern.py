# https://leetcode.com/problems/repeated-substring-pattern/submissions/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)  
        substr = "" 
        for i in range(n//2):
            substr+=s[i]  
            if n%len(substr)==0:
                if substr*(n//len(substr))==s:
                    return True
        return False   
ob = Solution()
s = "abcabcabcabc"
ans = ob.repeatedSubstringPattern(s)
print(ans)
