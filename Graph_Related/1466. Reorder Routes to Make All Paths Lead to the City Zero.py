from typing import List 
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import deque, defaultdict
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))
        print(graph)
        queue = deque([0])
        visited=set([0])
        count = 0
        while queue:
            node = queue.popleft()
            for neighbour, node_reversable in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    count+=node_reversable
        return count
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3