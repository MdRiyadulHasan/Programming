class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num==0 or num%10
ob = Solution()
num = 526
result = ob.isSameAfterReversals(num)
print(result)