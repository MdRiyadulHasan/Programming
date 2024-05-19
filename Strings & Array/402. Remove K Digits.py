# https://leetcode.com/problems/remove-k-digits/description/ 

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k>0 and stack[-1]>n:
                stack.pop() 
                k-=1 
            stack.append(n) 
        if stack and k>0: 
            stack = stack[:-k] 
        res = "".join(stack) 
        res = res.lstrip("0") 
        return res if res else "0"

num = "1432219"
k = 3