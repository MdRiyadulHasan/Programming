# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n 
        res = 1
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m-1
                res =m
            else:
                l = m+1
        return res
        
if __name__ == '__main__':
    n = 5
    bad = 4
    ob = Solution()
    result = ob.firstBadVersion(n)
    print(result)
