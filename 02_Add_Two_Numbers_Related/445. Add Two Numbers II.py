# https://leetcode.com/problems/add-two-numbers-ii/description/
from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(node):
            prev = None 
            while node:
                nextNode = node.next
                node.next = prev 
                prev = node 
                node = nextNode
            return prev 
        
        l3 = reverseList(l1)
        l4 = reverseList(l2)
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l3 or l4:
            val1 = l3.val if l3 else 0
            val2 = l4.val if l4 else 0
            addition = val1 + val2 + carry 
            rem = addition % 10
            carry = addition // 10
            current.next = ListNode(rem)
            current = current.next
            l3 = l3.next if l3 else None 
            l4 = l4.next if l4 else None 

        if carry:
            current.next = ListNode(carry)

        return reverseList(dummy.next)

# Example linked lists: 342 (2 -> 4 -> 3) and 465 (5 -> 6 -> 4)
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

       