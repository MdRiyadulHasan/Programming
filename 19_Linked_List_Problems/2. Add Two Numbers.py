# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy 
        carray = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            addition = val1+val2+carray 
            carray = addition//10
            rem = addition%10
            current.next = ListNode(rem)
            current = current.next 
            l1 = l1.next if l1 else None  
            l2 = l2.next if l2 else None  
        if carray:
            current.next = ListNode(carray)
        return dummy.next
        