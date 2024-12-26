# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, root.val)])
        count=0
        while queue:
            node, max_val = queue.popleft()
            if node.val>=max_val:
                count+=1
            new_max = max(node.val, max_val)
            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))
        return count
        
        