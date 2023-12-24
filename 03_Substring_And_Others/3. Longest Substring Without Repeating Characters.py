# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        maxLength = 0
        result = ''

        for ch in s:
            if ch not in result:
                result += ch
            else:
                result = result[result.index(ch) + 1:] + ch
            maxLength = max(maxLength, len(result))

        return maxLength

# Example
ob = Solution()
s = "abcabcbb"
result = ob.lengthOfLongestSubstring(s)
print(result)