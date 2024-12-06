from typing import List 
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for i, n in enumerate(groupSizes):
            dic[n].append(i)
        print(dic)
        result = []
        for k, v in dic.items():
            for i in range(0, len(v), k):
                result.append(v[i:i+k])
        return result