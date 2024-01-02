# Definition for singly-linked list.
# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Move to the node before the reversal starts
        for _ in range(left - 1):
            pre = pre.next

        # Reverse the sublist from left to right
        current = pre.next
        prev = None

        for _ in range(right - left + 1):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        # Connect the reversed sublist back to the original list
        pre.next.next = current
        pre.next = prev

        return dummy.next
# Example usage
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create an example linked list: 1 -> 2 -> 3 -> 4 -> 5
original_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head = solution.reverseBetween(original_head, 2, 4)

# Print the original and reversed linked lists
print("Original Linked List:")
print_linked_list(original_head)

print("\nReversed Linked List between positions 2 and 4:")
print_linked_list(reversed_head)
