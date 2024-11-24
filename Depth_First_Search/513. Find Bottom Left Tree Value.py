# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        def dfs(root, depth):
            nonlocal max_depth, bottom_left_val

            if not root:
                return
            if depth>max_depth:
                max_depth = depth
                bottom_left_val = root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        max_depth = -1
        bottom_left_val = None
        dfs(root,0)
        return bottom_left_val
        