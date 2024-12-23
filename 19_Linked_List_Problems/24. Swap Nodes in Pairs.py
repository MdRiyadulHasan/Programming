# https://leetcode.com/problems/swap-nodes-in-pairs/description/ 

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            node1 = current.next
            node2 = current.next.next
            current.next = node2
            node2.next = node1
            node1.next = node2.next
            current = node1
        return dummy.next
# Second Solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first_node = head 
            second_node = head.next 

            prev.next = second_node 
            first_node.next = second_node.next
            second_node.next= first_node 
            prev = first_node
            head = first_node.next
        return dummy.next
        