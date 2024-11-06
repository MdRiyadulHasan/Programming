# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==head:
            return
        prev = None
        current = head
        for _ in range(left-1):
            prev = current
            current = current.next
        start = prev
        end = current
        for _ in range(right-left+1):
            nextNode = current.next
            current.next = prev
            prev = current 
            current = nextNode
        if start:
            start.next=prev
        else:
            head = prev
        end.next = current
        return head


