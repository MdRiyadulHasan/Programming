class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i","o","u"}
        maxcount = 0 
        count = 0 
        for i, ch in enumerate(s):
            if ch in vowels:
                count+=1 
            if i>=k and s[i-k] in vowels:
                count-=1 
            maxcount = max(count, maxcount)
        return maxcount

s = "leetcode"
k = 3