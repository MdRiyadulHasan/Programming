# https://leetcode.com/problems/first-bad-version/

class Solution:
    class Solution:
        def firstBadVersion(self, n: int) -> int:
            l = 1
            r = n 
            while l<r:
                m = (l+r)//2
                if isBadVersion(m):
                    r = m
                else:
                    l = m+1
            return r
if __name__ == '__main__':
    n = 5
    bad = 4
    ob = Solution()
    result = ob.firstBadVersion(n)
    print(result)
