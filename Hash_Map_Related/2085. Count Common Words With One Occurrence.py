from typing import List 
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        return sum(1 for word, freq in freq1.items() if freq==1 and freq2[word]==1)