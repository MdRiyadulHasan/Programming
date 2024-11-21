from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        middleRow =set( "asdfghjkl")
        lastRow =set( "zxcvbnm")
        def can_type(word):
            word1 = set(word.lower())
            return word1<=firstRow or word1<=middleRow or word1 <=lastRow
        result = [word for word in words if can_type(word)]
        return result

        

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]