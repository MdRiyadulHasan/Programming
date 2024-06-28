class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            stack = []
            for ch in string:
                if ch!="#":
                    stack.append(ch)  
                elif stack:
                    stack.pop()
            return stack 
        return process_string(s)==process_string(t)   
s ="y#fo##f"
t ="y#f#o##f"
ob = Solution()
ans = ob.backspaceCompare(s,t)
print(ans)
