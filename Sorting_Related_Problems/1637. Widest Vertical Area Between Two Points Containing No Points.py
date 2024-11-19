from typing import List 
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[0])
        maxWidth = 0
        for i in range(1, len(points)):
            maxWidth = max(maxWidth, points[i][0]-points[i-1][0])
        return maxWidth
def maxWidthOfVerticalArea(points):
    # Extract x-coordinates
    x_coords = sorted(point[0] for point in points)
    
    # Compute the maximum difference between consecutive x-coordinates
    max_width = max(x_coords[i] - x_coords[i - 1] for i in range(1, len(x_coords)))
    
    return max_width

# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3