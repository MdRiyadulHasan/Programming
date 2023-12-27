# https://leetcode.com/problems/valid-palindrome-iv/description/

class Solution:
    def makePalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        cnt = 0
        while l < r:
            if s[l] != s[r]:
                cnt += 1
                if cnt > 2:
                    return False
            l += 1
            r -= 1
        return True
s = "abcdba"
ob = Solution()
result = ob.makePalindrome(s)
print(result)