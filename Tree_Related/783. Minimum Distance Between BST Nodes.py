# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root) -> int:
        def inorder(root):
            nonlocal prev, min_diff
            if not root:
                return
            inorder(root.left)

            if prev is not None:
                min_diff = min(min_diff, root.val-prev)
            prev = root.val

            inorder(root.right)
        min_diff = float("inf")
        prev = None
        inorder(root)
        return min_diff