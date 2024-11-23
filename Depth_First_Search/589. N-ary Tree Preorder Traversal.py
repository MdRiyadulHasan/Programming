"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def preorder(root):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                preorder(child)
        preorder(root)
        return result