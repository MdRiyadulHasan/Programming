# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            addition = val1 + val2 + carry
            rem = addition % 10
            carry = addition // 10
            current.next = ListNode(rem)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            current.next = ListNode(carry)
        
        return dummy.next

# Example usage:
# Create two linked lists representing the numbers 243 and 465
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Create an instance of the Solution class
solution = Solution()

# Call the addTwoNumbers function
result = solution.addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next
