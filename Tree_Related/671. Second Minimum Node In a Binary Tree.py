# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root) -> int:
        from collections import deque
        if not root:
            return -1
        min_val = root.val
        queue = deque([root])
        second_min = float("inf")
        while queue:
            node = queue.popleft()
            if min_val<node.val<second_min:
                second_min = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return second_min if second_min<float('inf') else -1
        