from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        index_map = {val:idx for idx,val in enumerate(inorder)}
        print(index_map)
        def helper(left,right):
            if left>right:
                return None 
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_index = index_map[root_val]
            root.right = helper(root_index+1, right)
            root.left = helper(left, root_index-1)
            return root
        return helper(0, len(inorder)-1)
        