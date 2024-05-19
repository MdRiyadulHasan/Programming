class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        res=""
        for ch in s:
            if ch not in vowels:
                res+=ch 
        return res 

s = "leetcodeisacommunityforcoders"