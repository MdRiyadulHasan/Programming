# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        stack = [root]
        left_sum = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                left_sum+=node.left.val
           
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return left_sum
        