from typing import List 
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {char:idx for idx, char in enumerate(s)}
        print(dic)
        start, end = 0,0
        result = []
        for i, ch in enumerate(s):
            end = max(end, dic[ch])
            if i==end:
                result.append(end-start+1)
                start = i+1
        return result