class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter 
        dic = Counter(s) 
        odd = 0
        for k,v in dic.items():
            if v%2:
                odd+=1
            if odd>1:
                return False  
        return True  

s = "carerac"
ob = Solution()
result = ob.canPermutePalindrome(s)
print(result)
