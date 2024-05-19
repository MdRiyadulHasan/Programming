from typing import List 
class Solution:
    def compress(self, chars: List[str]) -> int:
        import itertools 
        arr = []
        for key, group in itertools.groupby(chars):
            arr.append(key) 
            repeat = len(list(group)) 
            if repeat>1:
                arr.extend(list(str(repeat))) 
        chars[:] = arr 
        return len(chars)

chars = ["a","a","b","b","c","c","c"]     