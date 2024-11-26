from typing import List 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            # Mark the current city as visited
            visited[node] = True
            # Visit all its neighbors
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for i in range(n):
            if not visited[i]:
                # Start a new DFS for a new province
                dfs(i)
                province_count += 1

        return province_count