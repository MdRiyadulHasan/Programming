# https://leetcode.com/problems/add-binary/description/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)-1
        l2 = len(b)-1
        carray = 0
        res = ""
        while l1>=0 or l2>=0:
            val1 = int(a[l1]) if l1>=0 else 0
            val2 = int(b[l2]) if l2>=0 else 0
            addition = val1+val2+carray 
            rem = addition%2
            carray = addition//2
            res = str(rem)+res  
            l1-=1
            l2-=1
        if carray:
            res = str(carray) + res  
        return res 

a = "1010"
b = "1011"
ob = Solution()
result = ob.addBinary(a,b)
print(result)