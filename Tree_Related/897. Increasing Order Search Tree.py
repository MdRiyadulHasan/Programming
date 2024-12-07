# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            nonlocal last_node
            if not root:
                return
            inorder(root.left)
            root.left = None
            last_node.right = root
            last_node = root
            inorder(root.right)
            
        
        dummy = TreeNode(0)
        last_node = dummy
        inorder(root)
        return dummy.right