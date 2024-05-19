# 1313. Decompress Run-Length Encoded List

from typing import List 
class Solution:
    def decompressRLElist(self, N: List[int]) -> List[int]:
        L= len(N)
        A = []
        for i in range(0,L,2):
            A.extend(N[i]*[N[i+1]])
        return A
		