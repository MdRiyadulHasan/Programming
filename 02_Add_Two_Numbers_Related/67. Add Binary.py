# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        result = ""
        carry = 0

        while i >= 0 or j >= 0:
            aBit = int(a[i]) if i >= 0 else 0
            bBit = int(b[j]) if j >= 0 else 0
            total = aBit + bBit + carry
            rem = total % 2
            carry = total // 2
            result = str(rem) + result
            i = i - 1
            j = j - 1

        if carry:
            result = str(carry) + result

        return result

# Example usage:
sol = Solution()
binary_sum = sol.addBinary("1010", "1011")
print("Binary Sum:", binary_sum)
