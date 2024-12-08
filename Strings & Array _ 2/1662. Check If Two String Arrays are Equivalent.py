from typing import List 
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for ch in word1:
            str1+=ch
        for ch in word2:
            str2+=ch
        return str1==str2
        