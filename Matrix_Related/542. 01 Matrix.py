from typing import List 
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows = len(mat)
        cols = len(mat[0])
        result = [[float("inf")]*cols for _ in range(rows)]
        print("result",result)
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    result[r][c]=0
                    queue.append((r,c))
        print("Queue", queue)

        
        while queue:
            x,y=queue.popleft()
            directions = [(-1,0), (1,0),(0,1), (0,-1)]
            for dr, dc in directions:
                nx,ny = dr+x, dc+y
                if 0<=nx<rows and 0<=ny<cols:
                    if result[nx][ny]>result[x][y]+1:
                        result[nx][ny]=result[x][y]+1
                        queue.append((nx,ny))
                        
        return result
            