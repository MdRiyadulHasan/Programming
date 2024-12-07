# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeafNodes(root, leaves):
            if not root:
                return []
            if not root.left and not root.right:
                return leaves.append(root.val)
                
            findLeafNodes(root.left, leaves)
            findLeafNodes(root.right, leaves)  
        leaves1 = []
        leaves2 = []
        findLeafNodes(root1, leaves1)
        findLeafNodes(root2, leaves2)
        return leaves1==leaves2