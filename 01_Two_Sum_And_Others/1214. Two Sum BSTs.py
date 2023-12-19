# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        nums1 = []
        nums2 = []

        def inOrderTraversal(node, nums):
            if not node:
                return
            inOrderTraversal(node.left, nums)
            nums.append(node.val)
            inOrderTraversal(node.right, nums)

        inOrderTraversal(root1, nums1)
        inOrderTraversal(root2, nums2)

        l = 0
        r = len(nums2) - 1
        while l < len(nums1) and r >= 0:
            currentSum = nums1[l] + nums2[r]
            if currentSum == target:
                return True
            elif currentSum < target:
                l = l + 1
            else:
                r = r - 1

        return False

# Construct two sample binary search trees
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

solution = Solution()

# Check if there exist two elements, one from each tree, that sum up to 5
target_sum = 5
result = solution.twoSumBSTs(root1, root2, target_sum)

print(result)
