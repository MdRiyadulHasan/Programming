# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def isvalid(left, root, right):
            if not root:
                return True
            if not(left<root.val and root.val<right):
                return False 
            return (isvalid(left, root.left, root.val) and isvalid(root.val, root.right, right))

        
        return isvalid(float('-inf'), root, float('inf'))
        