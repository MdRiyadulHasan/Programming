# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        temp = fast
        while temp:
            slow = slow.next
            temp = temp.next
        slow.val, fast.val = fast.val, slow.val
        return dummy.next
            