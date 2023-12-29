#  00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0
        for _ in range(32):
            # Shift the result to the left and add the rightmost bit of n
            reversed_bits = (reversed_bits << 1) | (n & 1)
            # Move to the next bit in n
            n >>= 1
        return reversed_bits

# Example usage:
solution = Solution()
output = solution.reverseBits(43261596)
print(output)
