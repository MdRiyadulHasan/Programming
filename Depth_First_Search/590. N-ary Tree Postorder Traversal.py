"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node'):
        result = []
        def postorder(root):
            if not root:
                return
            for child in root.children:
                postorder(child)
            result.append(root.val)
        postorder(root)
        return result