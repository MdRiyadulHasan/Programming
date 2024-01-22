# https://leetcode.com/problems/rank-transform-of-an-array/

from typing import List 
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        arr1 = sorted(set(arr))
        result = []
        for i, n in enumerate(arr1):
            dic[n]=i+1
        for num in arr:
            result.append(dic[num])
        return result
if __name__ == '__main__':
    arr = [40,10,20,30]
    ob = Solution()
    result = ob.arrayRankTransform(arr)
    print(result)

