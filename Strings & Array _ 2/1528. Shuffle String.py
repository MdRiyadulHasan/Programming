from typing import List 
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = list(s)
        for ch, idx in zip(s,indices):
            new_s[idx]=ch
        return "".join(new_s)