from typing import List 
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from itertools import combinations
        def calculate_traingle(p1,p2,p3):
            return abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2
            
        max_area = 0
        for p1, p2, p3 in combinations(points,3):
            max_area = max(max_area, calculate_traingle(p1,p2,p3))
        return max_area 
    