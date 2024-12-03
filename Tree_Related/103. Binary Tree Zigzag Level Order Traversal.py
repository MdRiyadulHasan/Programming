# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(root):
        from collections import deque
        if not root:
            return []
        queue = deque([root])
        flag = False
        result = []
        while queue:
            level_count = len(queue)
            levels = []
            for _ in range(level_count):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not flag:
                result.append(levels)
                flag = True
            else:
                result.append(levels[::-1])
                flag = False
        return result
                