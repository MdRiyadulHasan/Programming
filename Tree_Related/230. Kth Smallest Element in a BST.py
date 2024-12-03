# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        from collections import deque
        if not root:
            return
        queue = deque([root])
        result = []
        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        result.sort()
        return result[k-1]
