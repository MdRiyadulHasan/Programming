from typing import List 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] + a < 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] + a == 0:
                    stack.pop()
        return stack 
ob = Solution()
asteroids = [10,2,-5]
result = ob.asteroidCollision(asteroids)
print(result)