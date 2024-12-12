from typing import List 
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        lengths = []
        bitmasks = []
        for word in words:
            mask = 0
            for char in word:
                mask|=1<<(ord(char)-ord("a"))
            bitmasks.append(mask)
            lengths.append(len(word))
        maxProduct = 0  
        for i in range(n):
            for j in range(i+1,n):
                if bitmasks[i]&bitmasks[j] == 0:
                    maxProduct = max(maxProduct, lengths[i]*lengths[j])
        return maxProduct