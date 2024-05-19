from typing import List 
class Solution:
    def compress(self, chars: List[str]) -> int:
        import itertools
        arr=[]
        for key,grp in itertools.groupby(chars):
            print(key, "...", grp)
            arr.append(key)                   # append the letter "a","b",...
            repeat=len(list(grp))  
            print("repeat", repeat)           # number of repeats of that letter
            if repeat>1:                      # only extend if repeats>1
                arr.extend(list(str(repeat))) # extend a list of str. For example: list(str(12))=["1","2"]
        chars[:]=arr
ob = Solution()
chars = ["a","a","b","b","c","c","c"]
result = ob.compress(chars)
print(result)