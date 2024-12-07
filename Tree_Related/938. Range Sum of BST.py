# Definition for a binary tree node.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        from collections import deque
        queue = deque([root])
        range_sum = 0
        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                if node.val>=low and node.val<=high:
                    range_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return range_sum