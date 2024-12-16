from typing import List 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node==len(graph)-1:
                result.append(path[:])
                return
            for neighbour in graph[node]:
                path.append(neighbour)
                dfs(neighbour, path)
                path.pop()
        result = []
        dfs(0,[0])
        return result