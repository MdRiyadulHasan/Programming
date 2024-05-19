class Solution:
    def compress(self, chars: List[str]) -> int:
        import itertools
        arr=[]
        for key,grp in itertools.groupby(chars):
            arr.append(key)                   # append the letter "a","b",...
            repeat=len(list(grp))             # number of repeats of that letter
            if repeat>1:                      # only extend if repeats>1
                arr.extend(list(str(repeat))) # extend a list of str. For example: list(str(12))=["1","2"]
        chars[:]=arr