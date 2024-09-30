from typing import List 
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter 
        common_count = Counter(words[0])
        for word in words[1:]:
            word_count = Counter(word)
            common_count&=word_count
        res = []
        for key, val in common_count.items():
            res.extend([key]*val)
        return res
words = ["bella","label","roller"]
# ["e","l","l"]