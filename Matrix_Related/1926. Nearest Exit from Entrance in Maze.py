from typing import List 
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        maze[entrance[0]][entrance[1]]="+"
        while queue:
            r,c,steps = queue.popleft()
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==".":
                    if nr==0 or nr==rows-1 or nc==0 or nc==cols-1:
                        return steps+1
                    maze[nr][nc]="+"
                    queue.append((nr, nc, steps+1))
        return -1



        