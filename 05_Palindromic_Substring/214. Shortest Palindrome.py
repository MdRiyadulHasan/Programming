# https://leetcode.com/problems/shortest-palindrome/
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]

        for i in range(len(t)):
            if s.startswith(t[i:]):
                return t[:i] + s

        return t + s
s = "aacecaaa"
ob = Solution()
res = ob.shortestPalindrome(s)
print(res)
