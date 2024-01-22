from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i,ch in enumerate(words):
            if x in ch:
                result.append(i) 
        return result