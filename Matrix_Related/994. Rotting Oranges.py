from typing import List 
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        queue = deque()
        fresh_orange = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_orange += 1
        if fresh_orange == 0:
            return 0
        minutes = 0
        directions = [(1,0),(-1,0), (0,1),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        queue.append((nx,ny))
                        fresh_orange -=1
            if queue:
                minutes += 1
        return minutes if fresh_orange==0 else -1