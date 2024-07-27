class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            print("a:--", bin(a))
            print("b--",bin(b))
            
            carry = ( a & b ) << 1
            print("carry:--", bin(carry))
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
ob = Solution()
a = 250
b = 430
ans = ob.getSum(a,b)
print(ans)