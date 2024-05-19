from typing import List 
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s,l,r):
            while l<r:
                s[l],s[r] = s[r], s[l]
                l+=1 
                r-=1
        n = len(s)
        reverse(s,0,n-1)

        l = 0 
        for r in range(n):
            if s[r]==" ":
                reverse(s,l,r-1)
                l = r+1 
        reverse(s,l,n-1)