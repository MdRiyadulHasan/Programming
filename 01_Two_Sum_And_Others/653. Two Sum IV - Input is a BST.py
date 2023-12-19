from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []

        def inOrderTraversal(node, nums):
            if not node:
                return
            inOrderTraversal(node.left, nums)
            nums.append(node.val)
            inOrderTraversal(node.right, nums)

        inOrderTraversal(root, nums)

        l = 0
        r = len(nums) - 1
        while l < r:
            currentSum = nums[l] + nums[r]
            if currentSum == k:
                return True
            elif currentSum < k:
                l = l + 1
            else:
                r = r - 1
        return False
    
# Construct a sample binary search tree
#root = [5,3,6,2,4,null,7]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Create an instance of the Solution class
solution = Solution()

# Check if there are two nodes in the tree with a sum of 9
target = 9
result = solution.findTarget(root, target)
print(result)