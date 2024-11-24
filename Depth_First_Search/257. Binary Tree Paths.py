# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        stack =[(root, str(root.val))]
        result = []
        while stack:
            root, path = stack.pop()
            if not root.left and not root.right:
                result.append(path)
            else:
                if root.left:
                    stack.append((root.left, path+"->"+str(root.left.val)))
                if root.right:
                    stack.append((root.right, path+"->"+str(root.right.val)))
        return result
