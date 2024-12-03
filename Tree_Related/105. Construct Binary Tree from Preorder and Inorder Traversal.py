# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        index_map = {val:idx for idx, val in enumerate(inorder)}
        preorder_index = 0
        def helper(left,right):
            nonlocal preorder_index
            if left>right:
                return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            root_index = index_map[root_val]
            preorder_index+=1
            root.left = helper(left, root_index-1)
            root.right = helper(root_index+1, right)
            return root 
        return helper(0, len(preorder)-1)
               