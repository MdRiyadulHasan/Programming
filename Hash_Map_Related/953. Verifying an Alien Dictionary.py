from typing import List 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dic = {ch:i for i, ch  in enumerate(order)}
        print(alien_dic)
        for i in range(len(words)-1):
            for c1, c2 in zip(words[i], words[i+1]):
                if alien_dic[c1]<alien_dic[c2]:
                    break
                elif alien_dic[c1]>alien_dic[c2]:
                    return False
            else:
                if len(words[i])>len(words[i+1]):
                    return False
        return True