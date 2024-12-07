from typing import List 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = 0
        for words in sentences:
            word = words.split()
            word_count = len(word)
            if word_count>max_word:
                max_word = word_count
        return max_word