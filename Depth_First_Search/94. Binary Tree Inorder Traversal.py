# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result
# Input: root = [1,null,2,3]

# Output: [1,3,2]