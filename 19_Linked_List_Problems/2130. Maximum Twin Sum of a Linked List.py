# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        max_sum = 0
        first_half = head
        second_half = prev
        while second_half:
            sum_value = first_half.val+second_half.val
            max_sum = max(max_sum, sum_value)
            first_half = first_half.next
            second_half = second_half.next
        return max_sum
        