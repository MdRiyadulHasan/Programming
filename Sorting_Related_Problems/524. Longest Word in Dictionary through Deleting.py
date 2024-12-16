from typing import List 
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        print(dictionary)
        def isSubsequence(word):
            it = iter(s)
            print(it)
            return all(char in it for char in word)

        for word in dictionary:
            if isSubsequence(word):
                return word
        return ""