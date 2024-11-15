class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if n==0:
            return 0
        for i in range(h-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
haystack = "sadbutsad"
needle = "sad"