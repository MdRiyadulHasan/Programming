from typing import List 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        print (result)
        for i in range(1, len(intervals)):
            prev = result[-1]
            current = intervals[i]
            if current[0]<=prev[1]:
                prev[1]=max(current[1], prev[1])
            else:
                result.append(current)
        return result
intervals = [[1,4],[2,3]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
        