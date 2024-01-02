# https://leetcode.com/problems/reverse-linked-list/description/ 

from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create an example linked list: 1 -> 2 -> 3 -> 4 -> 5
original_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head = solution.reverseList(original_head)
print("\nReversed Linked List:")
print_linked_list(reversed_head)

