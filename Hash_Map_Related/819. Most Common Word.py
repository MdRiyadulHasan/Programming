from typing import List 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re 
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)
        word_dic = Counter(word for word in words if word not in banned_set)
        return word_dic.most_common(1)[0][0]