# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        maxLength = 0
        dic = {}
        count = 0
        left = 0

        for right, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1

            if dic[ch] == 1:
                count += 1

            while count > 2:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    count -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength

# Example
ob = Solution()
s = "eceba"
result = ob.lengthOfLongestSubstringTwoDistinct(s)
print(result)