"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root) -> int:
        from collections import deque
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth+=1
            level_count = len(queue)
          
            for _ in range(level_count): 
                node = queue.popleft()
                if node.children:
                    queue.extend(node.children)
        return depth
