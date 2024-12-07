from typing import List 
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        words = s1.split()+s2.split()
        print(words)
        word_dic = Counter(words)
        return[word for word, count in word_dic.items() if count==1]