# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        if not root:
            return []
        def inorder(root):
            nonlocal prev, count, max_count, modes
            if not root:
                return 
            inorder(root.left)
            if root.val==prev:
                count+=1
            else:
                count = 1
                prev = root.val
            if count>max_count:
                max_count = count
                modes = [root.val]
            elif max_count==count:
                modes.append(root.val)
            inorder(root.right)
        

        prev = None
        count = 0
        max_count = 0
        modes = []
        inorder(root)
        return modes