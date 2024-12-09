class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        product = 1
        addition = 0
        for ch in n:
            product*=int(ch)
            addition +=int(ch)
        return product-addition
# Input: n = 4421
# Output: 21
