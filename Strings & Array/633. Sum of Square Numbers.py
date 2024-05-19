class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c**0.5)
        while l<=r:
            current_sum = l *l + r * r
            if current_sum == c :
                return True
            elif current_sum < c:
                l = l+1
            else:
                r = r - 1
        return False