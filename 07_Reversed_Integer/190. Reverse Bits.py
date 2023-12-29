# https://leetcode.com/problems/reverse-bits/description/
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res

# Example usage:
solution = Solution()
output = solution.reverseBits(43261596)
print(output)
