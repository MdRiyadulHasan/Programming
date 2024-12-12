from typing import List 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for ch in logs:
            if stack and ch=="../":
                stack.pop()
            elif ch=="./":
                continue
            elif ch!="../":
                stack.append(ch)
        return len(stack)
        