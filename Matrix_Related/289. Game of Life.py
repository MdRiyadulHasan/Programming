from typing import List 
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def count_live_neighbours(r,c):
            directions = [(-1,-1), (-1,0), (-1,1),
                        (0,-1),(0,1),
                        (1,-1), (1,0), (1,1)
                        ]
            count=0
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and abs(board[nr][nc])==1:
                    count+=1
            return count
        for r in range(rows):
            for c in range(cols):
                live_neighbours = count_live_neighbours(r,c)
                
                if board[r][c]==1 and (live_neighbours<2 or live_neighbours>3):
                    board[r][c] = -1
                elif board[r][c]==0 and live_neighbours==3:
                    board[r][c] = 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==-1:
                    board[r][c] = 0
                elif board[r][c]==2:
                    board[r][c] = 1