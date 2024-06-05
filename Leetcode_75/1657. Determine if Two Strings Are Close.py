class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter 
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)
        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())
        match_keys = frequency_word1.keys()==frequency_word2.keys()
        return sorted_values_word1==sorted_values_word2 and match_keys
        