"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root) :
        from collections import deque
        if not root:
            return
        queue = deque([root])
        result = []
        while queue:
            levels = []
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                levels.append(node.val)
                queue.extend(node.children)
            result.append(levels)
        return result
        