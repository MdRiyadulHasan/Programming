# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s)<=k:
            return len(s)
        maxLength = 0
        dic = {}
        count = 0
        left = 0

        for right, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1

            if dic[ch] == 1:
                count += 1

            while count > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    count -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
s = "eceba"
k = 2
ob = Solution()
result = ob.lengthOfLongestSubstringKDistinct(s,k)
print(result)