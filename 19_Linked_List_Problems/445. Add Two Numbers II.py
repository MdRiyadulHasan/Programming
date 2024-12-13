# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            # if not head or head.next:
            #     return head
            prev = None
            current = head
            while current:
                nextNode = current.next
                current.next = prev 
                prev = current
                current = nextNode
            return prev
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        carry=0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1+val2+carry
            carry = total//10
            rem = total%10
            current.next = ListNode(rem)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return reverseList(dummy.next)
        

        