# https://leetcode.com/problems/palindrome-linked-list/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l]!=nums[r]:
                return False
            l = l + 1
            r = r -1
        return True
# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
result = solution.isPalindrome(node1)
print(result)  # Output: True



