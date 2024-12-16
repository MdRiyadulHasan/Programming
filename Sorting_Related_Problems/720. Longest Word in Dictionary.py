from typing import List 
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        result = ""
        word_set = set([""])
        print(word_set)
        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word)>len(result):
                    result = word
        return result