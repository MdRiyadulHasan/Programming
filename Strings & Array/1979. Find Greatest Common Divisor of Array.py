from typing import List 

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a
        a = min(nums)
        b= max(nums)
        ans = gcd(a,b)
        return ans
       
nums = [2,5,6,9,10]
ob = Solution() 
res = ob.findGCD(nums)