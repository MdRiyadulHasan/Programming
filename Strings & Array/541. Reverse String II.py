class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k]) 
        return "".join(s)


s = "abcdefg"
k = 2
ob = Solution()
ans = ob.reverseStr(s,k)
print(ans)