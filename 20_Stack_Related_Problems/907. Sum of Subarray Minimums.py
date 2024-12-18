from typing import List 
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        n = len(arr)
        P = [0]*n
        N = [0]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            P[i]=i-stack[-1] if stack else i+1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            N[i]=stack[-1]-i if stack else n-i
            stack.append(i)
        result = 0
        for i in range(n):
            result+=arr[i]*P[i]*N[i]
            result = result%MOD
        return result
# Input: arr = [3,1,2,4]
# Output: 17