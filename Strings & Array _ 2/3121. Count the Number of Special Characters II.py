import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for ch, CH in zip(lowercase, uppercase):

            if ch not in word or CH not in word: continue
  
            ans+= word.rfind(ch) < word.find(CH)

        return ans